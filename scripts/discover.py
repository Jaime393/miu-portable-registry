#!/usr/bin/env python3
"""Read a bounded public discovery snapshot. No network, credentials or execution."""
import argparse
from datetime import datetime
import json
from pathlib import Path
import re
import sys

DEFAULT_CATALOG = Path(__file__).resolve().parents[1] / "catalog" / "capabilities.json"
MAX_BYTES = 5 * 1024 * 1024


def require(condition, reason):
    if not condition:
        raise ValueError(reason)


def validate(catalog):
    require(isinstance(catalog, dict), "catalog must be an object")
    require(catalog.get("schema") == "miu.repository-catalog/v1", "unsupported schema")
    require(catalog.get("auto_apply") is False, "auto_apply must be false")
    stamp = catalog.get("observed_at", "")
    require(isinstance(stamp, str) and stamp.endswith("Z"), "UTC timestamp required")
    datetime.fromisoformat(stamp.replace("Z", "+00:00"))
    repositories = catalog.get("repositories")
    fronts = catalog.get("fronts")
    capabilities = catalog.get("capabilities")
    require(isinstance(repositories, list), "repositories must be a list")
    require(isinstance(fronts, list), "fronts must be a list")
    require(isinstance(capabilities, list), "capabilities must be a list")
    by_id = {}
    names = set()
    for repo in repositories:
        require(isinstance(repo, dict), "repository must be an object")
        rid, name = repo.get("github_id"), repo.get("repository", "")
        require(type(rid) is int and rid > 0 and rid not in by_id, "invalid or duplicate github_id")
        require(isinstance(name, str) and re.fullmatch(r"[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+", name),
                "invalid repository name")
        require(name.casefold() not in names, "duplicate repository name")
        require(repo.get("visibility") == "public" and "private" not in repo, "public records only")
        require(repo.get("url") == f"https://github.com/{name}", "repository URL mismatch")
        require(repo.get("discovery") in {"metadata_only", "tree_inspected"}, "invalid discovery state")
        tree = repo.get("tree")
        if repo["discovery"] == "tree_inspected":
            require(isinstance(tree, dict), "tree evidence required")
            require(re.fullmatch(r"[0-9a-f]{40}", tree.get("revision", "")), "invalid tree revision")
            require(tree.get("truncated") is False, "partial trees are not complete evidence")
            require(type(tree.get("file_count")) is int and tree["file_count"] >= 0, "invalid file count")
            require(isinstance(tree.get("candidate_files"), list), "candidate files required")
            for entry in tree["candidate_files"]:
                path = entry.get("path", "")
                require(isinstance(path, str) and path and not path.startswith("/")
                        and ".." not in path.split("/"), "invalid candidate path")
                require(re.fullmatch(r"[0-9a-f]{40}", entry.get("sha", "")), "invalid file hash")
        else:
            require(tree is None, "metadata-only record cannot claim tree evidence")
        by_id[rid] = repo
        names.add(name.casefold())
    front_ids = set()
    for front in fronts:
        fid = front.get("front_id", "")
        require(isinstance(fid, str) and re.fullmatch(r"[a-z0-9-]+", fid)
                and fid not in front_ids, "invalid or duplicate front_id")
        refs = front.get("repository_ids")
        require(isinstance(refs, list) and all(type(rid) is int and rid in by_id for rid in refs),
                "front references unknown repository")
        require(len(refs) == len(set(refs)), "duplicate repository in front")
        front_ids.add(fid)
    capability_ids = set()
    for capability in capabilities:
        cid = capability.get("capability_id")
        require(isinstance(cid, str) and cid and cid not in capability_ids,
                "invalid or duplicate capability_id")
        rid = capability.get("repository_id")
        require(type(rid) is int and rid in by_id, "capability references unknown repository")
        require(capability.get("implementation_state") == "draft_local_tests_passed",
                "unsupported implementation state")
        pr = capability.get("pull_request", {})
        prefix = by_id[rid]["url"] + "/pull/"
        require(isinstance(pr.get("url"), str) and pr["url"].startswith(prefix)
                and pr["url"][len(prefix):].isdigit(), "PR URL mismatch")
        require(pr.get("draft") is True and pr.get("merged") is False, "draft scope required")
        require(re.fullmatch(r"[0-9a-f]{40}", pr.get("commit", "")), "invalid proposal commit")
        capability_ids.add(cid)
    return catalog


def load_catalog(path=DEFAULT_CATALOG):
    path = Path(path)
    require(path.stat().st_size <= MAX_BYTES, "catalog exceeds size limit")
    return validate(json.loads(path.read_text(encoding="utf-8")))


def discover(catalog, query="", front=None, github_id=None, limit=20):
    require(type(limit) is int and limit > 0, "limit must be positive")
    allowed = None
    if front is not None:
        match = next((item for item in catalog["fronts"] if item["front_id"] == front), None)
        require(match is not None, "unknown front")
        allowed = set(match["repository_ids"])
    terms = query.casefold().split()
    rows = []
    for repo in catalog["repositories"]:
        if allowed is not None and repo["github_id"] not in allowed:
            continue
        if github_id is not None and repo["github_id"] != github_id:
            continue
        paths = [item["path"] for item in repo.get("tree", {}).get("candidate_files", [])]
        haystack = " ".join([repo["repository"], *paths]).casefold()
        if not all(term in haystack for term in terms):
            continue
        rows.append(repo)
    rows.sort(key=lambda item: (item["repository"].casefold(), item["github_id"]))
    selected = rows[:limit]
    selected_ids = {row["github_id"] for row in selected}
    return {
        "schema": "miu.discovery-result/v1",
        "snapshot_observed_at": catalog["observed_at"],
        "matched": len(rows),
        "returned": len(selected),
        "repositories": selected,
        "capabilities": [item for item in catalog["capabilities"]
                         if item["repository_id"] in selected_ids],
        "auto_apply": False,
        "runtime_verified": False,
    }


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--catalog", type=Path, default=DEFAULT_CATALOG)
    parser.add_argument("--query", default="")
    parser.add_argument("--front")
    parser.add_argument("--id", dest="github_id", type=int)
    parser.add_argument("--limit", type=int, default=20)
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--validate", action="store_true")
    mode.add_argument("--list-fronts", action="store_true")
    args = parser.parse_args(argv)
    try:
        catalog = load_catalog(args.catalog)
        if args.validate:
            result = {"status": "valid", "repositories": len(catalog["repositories"]),
                      "fronts": len(catalog["fronts"]), "capabilities": len(catalog["capabilities"])}
        elif args.list_fronts:
            result = catalog["fronts"]
        else:
            result = discover(catalog, args.query, args.front, args.github_id, args.limit)
        print(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True))
        return 0
    except (OSError, ValueError, TypeError, AttributeError, KeyError) as error:
        print(f"Blocked: {error}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
