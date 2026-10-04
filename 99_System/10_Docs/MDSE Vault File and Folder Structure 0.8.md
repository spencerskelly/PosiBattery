# MDSE Vault File and Folder Structure — v0.8.0

## Purpose

This document is the filesystem contract for AI tools and engineers working in this vault. It describes the structure that must be preserved when creating, rebuilding, or reorganizing a compatible MDSE engineering vault.

It is subordinate to the active release metadata and schemas. For this vault:

- MDSE release: `0.8.0`
- Modeling ruleset: `1.23`
- Relationship schema: `1.35`
- Element schema: `1.17`
- Local Model schema: `0.2`

If a later controlled release changes these versions, the later release governs.

## 1. Core rule

Folder placement is navigation, not model semantics.

Do not infer `partOf`, `subtypeOf`, ownership, applicability, performance, or any other engineering relationship from a filesystem path. Engineering meaning lives in note type/subtype, governed properties, Local Model records, and relationships defined by the schemas.

## 2. Required vault-root infrastructure

A compatible engineering vault preserves these root-level infrastructure items:

```text
/
├── .gitattributes
├── .gitignore
├── .obsidian/
├── .vault.yaml
├── 99_System/
├── AGENTS.md
└── README.md
```

Project/model content folders live beside `99_System/`. Their names are domain-specific and are not part of the MDSE semantic contract.

### 2.1 `.vault.yaml`

Must retain:

```yaml
vault_uid: <initialized vault UID or UNINITIALIZED in a clean base>
name: <vault name>
default_branch: main
mdse_release: "0.8.0"
```

Do not remove or rewrite `mdse_release` during normal vault initialization.

### 2.2 `.obsidian/`

This is controlled runtime configuration. Preserve the issued plugin stack and configuration.

Current required configuration families include:

```text
.obsidian/
├── app.json
├── appearance.json
├── community-plugins.json
├── core-plugins.json
├── graph.json
├── plugin-lock.yaml
├── plugins/
├── templates.json
└── types.json
```

Do not independently install, remove, or update plugins when reconstructing a compatible vault. The release controls the plugin set.

## 3. Required `99_System/` runtime layout

The lean engineering runtime uses this structure:

```text
99_System/
├── 01_Admin/
│   └── Enabled Plugin Stack.md
├── 02_AI/
│   ├── 00 - Folder Contents.base
│   ├── 00 - Folder Map.canvas
│   ├── 00 - Views and Bases.md
│   └── AI_INSTRUCTIONS.md
├── 03_Schemas/
│   ├── authors.yaml
│   ├── business-relationships.provisional.yaml
│   ├── element-types.yaml
│   ├── local-model.yaml
│   └── relationships.yaml
├── 04_People/
│   └── <person notes>
├── 05_Templates/
│   └── <controlled class templates and navigation templates>
├── 06_Fileclasses/
│   └── <generated fileclasses>
├── 08_Scripts/
│   ├── 00 - Folder Contents.base
│   ├── 00 - Folder Map.canvas
│   ├── 00 - Views and Bases.md
│   └── 02_Snippets/
├── 09_Tools/
│   ├── Initialize-Vault.ps1
│   ├── Initialize-Vault.sh
│   └── check-links.py
├── 10_Docs/
│   ├── MDSE Modeling Ruleset 1.23.md
│   └── MDSE Vault File and Folder Structure 0.8.md
├── check-dependencies.py
└── check-names.py
```

The absence of a numbered folder such as `07_*` is intentional unless a controlled release introduces one.

### 3.1 What must not be copied into a lean engineering vault

Do not copy methodology-workspace-only material into a normal engineering vault merely because it exists in the MDSE development repository. In particular, the lean runtime intentionally omits methodology Current State files, release manifests, Translator Definition working material, Decision Logs, EA evidence, archives, and Workbench design notes unless a controlled release explicitly includes them.

## 4. Content folders

Model content belongs in meaningful domain-oriented folders at the root or below them.

The current PosiBattery root content areas are:

```text
Customer Actors/
Customer Needs/
Definitions/
Downloads/
Organizations/
Performance Metrics/
Product Designs/
Product Functions/
Products/
Research/
Source Documents/
```

These names document the current PosiBattery organization; they are not universal MDSE element classes and do not define semantic relationships.

When creating a new compatible vault, choose content folders that help humans navigate the model. Do not mechanically reproduce the PosiBattery folder names unless the new vault has the same domain needs.

## 5. Folder design rules

Use meaningful semantic/navigation subdivisions rather than arbitrary size buckets.

- Aim for roughly 5–6 meaningful folder levels below the root for normal model content.
- Deeper hierarchy is allowed when it preserves real architecture, source-document hierarchy, regulatory hierarchy, or another useful formal structure.
- Do not split a folder only because it exceeds an element-count target.
- Do not create arbitrary numbered overflow folders.
- Collapse an intermediate folder only when it has one meaningful child branch and no independent note, content, or navigation value.
- Do not emit empty folders for empty source packages.
- Folder names should normally be human-readable and aim for 40 characters or fewer, but this is a soft target rather than a truncation rule.
- Generated repository-relative paths must not exceed 212 characters after approved normalization.

## 6. Standard folder navigation artifacts

Do **not** create README/Base/Canvas scaffolding for every folder.

Automatically create the standard navigation set only for primary MDSE top-level domain folders:

```text
README_<folder>.md
BASE_local_<folder>.base
BASE_all_<folder>.base
CANVAS_<folder>.canvas
```

Lower-level folders receive navigation artifacts only when a demonstrated navigation need exists.

The artifacts serve different purposes:

- `README_<folder>`: explains what belongs in the area, where to start, and major related areas.
- `BASE_local_<folder>`: shows direct folder contents.
- `BASE_all_<folder>`: recursive view of descendants.
- `CANVAS_<folder>`: curated map, not exhaustive inventory; roughly 12–20 nodes is a useful soft target.

Do not put exhaustive generated inventories into README files.

## 7. Files and model notes

Every model note must be created from the matching controlled template in `99_System/05_Templates/` or be structurally identical to that template when created by an AI.

Current model classes include Actor, Artifact, Design, Diagram, Document, Failure Mode, Function, Functional Flow, Info, Issue, Item Flow, Object, Plan, Port, Procedure, Requirement, Result, Setup, State, State Machine, Step, Use Case, Verification, and governed supporting classes.

System/reference notes under `99_System/` do not receive normal model `type`/`subtype` frontmatter.

Do not create a new top-level element class or template merely to match a folder name.

## 8. Naming and collisions

Plain engineering names are reserved for model content. Infrastructure uses reserved patterns such as:

```text
Template - <Name>
Rule - <Name>
README_<folder>
BASE_local_<folder>
BASE_all_<folder>
CANVAS_<folder>
```

For generated duplicate or forced-alteration filenames/folders, use the v0.8 markers:

- duplicate: `Name~2`, `Name~3`, ...
- forced alteration: `Name~a`, `Name~b`, ...
- both: `Name~a~2`

Do not solve collisions with arbitrary `_1`, `_2` suffixes when meaningful context can provide a human-readable discriminator.

Ports use the filesystem form:

```text
i<shortest unambiguous owner label> - <Port Name>.md
```

The visible heading remains the Port name.

## 9. Source documents and imported files

External/source material is not automatically converted into an MDSE model note and must not be stamped with a newly invented MDSE `id` or `uid`.

Keep source material in an appropriate source/document area and preserve its own identification. Model notes may reference or describe it using governed relationships where appropriate.

Attachments and extracted source files should remain associated with their authoritative document/context using deterministic human-readable placement.

## 10. AI reconstruction procedure

An AI asked to build or repair a compatible vault should follow this order:

1. Read `AGENTS.md`.
2. Read `99_System/02_AI/AI_INSTRUCTIONS.md`.
3. Read `99_System/10_Docs/MDSE Modeling Ruleset 1.23.md`.
4. Read this filesystem contract.
5. Read `99_System/03_Schemas/element-types.yaml`, `relationships.yaml`, `local-model.yaml`, and `authors.yaml`.
6. Preserve the issued `.obsidian/`, `99_System/`, root control files, and `mdse_release`.
7. Create or reorganize content folders only for human navigation; never use folder placement as semantic evidence.
8. Create model notes from controlled templates and validate IDs, UIDs, relationships, inverses, and links before handoff.
9. Do not autonomously create or split vaults.
10. If a required runtime file is missing or a version mismatch exists, stop treating the vault as release-compatible and surface the mismatch instead of inventing a replacement.

## 11. Compatibility test

A filesystem should be considered structurally compatible with this release only when:

- the root infrastructure exists;
- `.vault.yaml` declares the expected `mdse_release`;
- the controlled `.obsidian/` runtime is preserved;
- the required `99_System/` schemas, templates, fileclasses, AI instructions, tools, and ruleset are present;
- content folders are navigational rather than semantic;
- standard navigation artifacts are limited to the intended primary-domain level unless a lower-level need is explicit;
- file/path naming follows the v0.8 conventions;
- model notes conform to the active templates and schemas.

When in doubt, preserve the controlled runtime and surface the uncertainty rather than generating a plausible but incompatible structure.
