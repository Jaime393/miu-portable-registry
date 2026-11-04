import copy
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("discover", ROOT / "scripts" / "discover.py")
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class DiscoveryTests(unittest.TestCase):
    def setUp(self):
        self.catalog = {
            "schema": "miu.repository-catalog/v1",
            "observed_at": "2026-11-04T02:00:00Z",
            "auto_apply": False,
            "repositories": [
                {"github_id": 1, "repository": "example/skills", "visibility": "public",
                 "url": "https://github.com/example/skills", "discovery": "metadata_only"},
                {"github_id": 2, "repository": "example/pva", "visibility": "public",
                 "url": "https://github.com/example/pva", "discovery": "tree_inspected",
                 "tree": {"revision": "a" * 40, "truncated": False, "file_count": 1,
                          "candidate_files": [{"path": "src/validator.py", "sha": "b" * 40}]}},
            ],
            "fronts": [{"front_id": "validation", "repository_ids": [2]}],
            "capabilities": [],
        }

    def test_real_snapshot_valid(self):
        catalog = MODULE.load_catalog()
        self.assertGreater(len(catalog["repositories"]), 200)
        self.assertTrue(all(row["visibility"] == "public" for row in catalog["repositories"]))
        self.assertGreaterEqual(len(catalog["fronts"]), 7)
        self.assertEqual(len(catalog["capabilities"]), 10)

    def test_path_query(self):
        result = MODULE.discover(MODULE.validate(self.catalog), query="VALIDATOR")
        self.assertEqual([row["github_id"] for row in result["repositories"]], [2])
        self.assertFalse(result["auto_apply"])
        self.assertFalse(result["runtime_verified"])

    def test_front_and_id(self):
        self.assertEqual(MODULE.discover(self.catalog, front="validation", github_id=2)["matched"], 1)
        self.assertEqual(MODULE.discover(self.catalog, front="validation", github_id=1)["matched"], 0)

    def test_unknown_front_blocked(self):
        with self.assertRaisesRegex(ValueError, "unknown front"):
            MODULE.discover(self.catalog, front="missing")

    def test_duplicate_id_blocked(self):
        self.catalog["repositories"][1]["github_id"] = 1
        with self.assertRaisesRegex(ValueError, "github_id"):
            MODULE.validate(self.catalog)

    def test_private_record_blocked(self):
        self.catalog["repositories"][0]["visibility"] = "private"
        with self.assertRaisesRegex(ValueError, "public records only"):
            MODULE.validate(self.catalog)

    def test_unknown_reference_blocked(self):
        self.catalog["fronts"][0]["repository_ids"] = [99]
        with self.assertRaisesRegex(ValueError, "unknown repository"):
            MODULE.validate(self.catalog)

    def test_url_mismatch_blocked(self):
        self.catalog["repositories"][0]["url"] = "https://example.invalid/login"
        with self.assertRaisesRegex(ValueError, "URL mismatch"):
            MODULE.validate(self.catalog)

    def test_partial_tree_and_traversal_blocked(self):
        bad = copy.deepcopy(self.catalog)
        bad["repositories"][1]["tree"]["truncated"] = True
        with self.assertRaisesRegex(ValueError, "partial trees"):
            MODULE.validate(bad)
        self.catalog["repositories"][1]["tree"]["candidate_files"][0]["path"] = "../secret"
        with self.assertRaisesRegex(ValueError, "candidate path"):
            MODULE.validate(self.catalog)

    def test_limit_and_order(self):
        result = MODULE.discover(self.catalog, limit=1)
        self.assertEqual((result["matched"], result["returned"]), (2, 1))
        self.assertEqual(result["repositories"][0]["repository"], "example/pva")
        with self.assertRaisesRegex(ValueError, "positive"):
            MODULE.discover(self.catalog, limit=0)

    def test_proposal_pr_scope(self):
        self.catalog["capabilities"] = [{
            "capability_id": "bounded-reader", "repository_id": 1,
            "implementation_state": "draft_local_tests_passed",
            "pull_request": {"url": "https://github.com/example/skills/pull/1",
                             "draft": True, "merged": False, "commit": "a" * 40},
        }]
        MODULE.validate(self.catalog)
        self.catalog["capabilities"][0]["pull_request"]["merged"] = True
        with self.assertRaisesRegex(ValueError, "draft scope"):
            MODULE.validate(self.catalog)

    def test_cli_success_and_malformed_input(self):
        result = subprocess.run([sys.executable, str(ROOT / "scripts/discover.py"), "--validate"],
                                capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(json.loads(result.stdout)["status"], "valid")
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "malformed.json"
            path.write_text("{invalid", encoding="utf-8")
            result = subprocess.run([sys.executable, str(ROOT / "scripts/discover.py"),
                                     "--catalog", str(path)], capture_output=True, text=True)
            self.assertEqual(result.returncode, 2)
            self.assertIn("Blocked:", result.stderr)


if __name__ == "__main__":
    unittest.main()
