# External Model Import Governance

EA or other model imports are staged, not written directly over the maintained vault. Preserve source identity and semantics, then promote reviewed content.

Required import registries live in `99_System/11_Import`:

1. Identity Registry — source GUID ↔ MDSE ID ↔ filepath.
2. Transformation Log — merges, collapses, semantic remaps, suppressions, renames.
3. Model Checks — ambiguity, naming, relationship and source-model issues.
4. Pending Relationships — cross-package endpoints not yet resolvable.

Imported notes may carry `eaGUID`. Source metaclasses belong in logs/diagnostics unless they have enduring engineering meaning. Never create placeholder engineering elements solely to close unresolved cross-package links.
