# Discovery contract

The catalog is a public snapshot, not an authority to execute code. Numeric GitHub repository IDs are used for joins; names, owners and branches can change.

## Evidence states

- **metadata_only:** the repository was returned by the authenticated GitHub API. Its name is not evidence that the advertised function works.
- **tree_inspected:** a complete file tree and file-object hashes were read at the recorded revision. `tree.revision` is the inspected Git reference, not a claim that a commit SHA is a root-tree object SHA; candidate paths are navigation hints, not proof that their contents are executable.
- **draft_local_tests_passed:** one specific implementation exists in an identified draft PR and passed the listed local checks. This is not a whole-repository certification, merge or deployment.

The catalog intentionally does not copy repository descriptions as capability claims. Private inventory is omitted, including private names and paths.

## How to continue

1. Validate the snapshot and query by front, ID or candidate path.
2. Recheck repository visibility and current branch/commit through an authorized connector or CLI.
3. Read instructions, actual source and workflow triggers before editing or running anything.
4. Reuse prior code when possible. Distinguish prose specifications from functioning programs.
5. Test the smallest useful capability without new credentials, costs or external effects.
6. Save a bounded result to an authorized remote location, then read it back.
7. Publish only safe pointers, evidence level, checks and next route. Do not publish account inventories, OTPs, secrets, private source paths or signed URLs.
8. Keep merge, deployment, scheduled execution, security changes and downstream absorption as separate states requiring their own evidence and authorization.

## Initial cross-repository links

The [audit generator draft](https://github.com/Jaime393/miu-tools/pull/1) provides deterministic, versioned audit artifacts with fourteen passing local tests. It does not itself persist those artifacts to the network.

The [checkpoint discovery skill draft](https://github.com/Jaime393/miu-portable-skills/pull/1) derives from prior methodology and includes a credential-free primary/replica reader with six mocked tests. Its earlier live reads and controlled fallback do not establish an autonomous recovery daemon.

The catalog and this reader make discovery actionable without claiming that the listed agents, PVA tools, models, Workers or historical documents have been validated. Reconcile and checkpoint each next front independently.

## Bounded capabilities connected in the second pass

- **Agent routing:** [miu-agents draft](https://github.com/Jaime393/miu-agents/pull/1) consults the pinned catalog reader before any provider execution. Eight local cases passed; no model or webhook was called.
- **Artifact readiness:** [pva-lint draft](https://github.com/Jaime393/pva-lint/pull/1) reports structural evidence, not scientific reproducibility. Eight local cases passed.
- **Local orchestration:** [pva-orchestrator draft](https://github.com/Jaime393/pva-orchestrator/pull/1) executed five pinned local capabilities with retained partial evidence. Twelve cases passed; Docker, Lean compilation/proof, external publication and adversarial validation remain unperformed.
- **CSV summary:** [pva-docker-template draft](https://github.com/Jaime393/pva-docker-template/pull/1) summarizes actual bounded CSV input without a dummy PNG or invented metrics. Seven cases passed; Docker was not built.
- **Formalization backlog:** [pva-lean-bridge draft](https://github.com/Jaime393/pva-lean-bridge/pull/1) preserves source claims in commented Lean files without manufacturing trivial proofs. Seven cases passed.
- **Local receipts:** [pva-ledger draft](https://github.com/Jaime393/pva-ledger/pull/1) hashes and verifies explicit file bytes without fabricated publication identifiers. Seven cases passed; no authorship or trusted timestamp is established.
- **Reported-paper registry:** [pva-swarm draft](https://github.com/Jaime393/pva-swarm/pull/1) offers local snapshots and opt-in loopback writes, not distributed validation. Seven cases passed.
- **Non-executing decoder:** [pva-api draft](https://github.com/Jaime393/pva-api/pull/1) separates matching checksums from authentication, authorization and execution. Nine cases passed; historical labels are data, not permission.

The snapshot now contains ten bounded capability proposals and fifteen inspected public trees across eight navigation fronts. Updated tree records explicitly identify draft-branch revisions; earlier tree evidence is retained as `previous_tree`. None of these drafts has been merged or deployed.
