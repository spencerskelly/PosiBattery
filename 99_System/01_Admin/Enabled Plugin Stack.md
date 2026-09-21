# Enabled Plugin Stack

The vault ships with the tested plugin binaries from the MDSE baseline and has them enabled in `.obsidian/community-plugins.json`.

| Plugin | Role in MDSE |
|---|---|
| MDSE Bootstrap | Portable plugin/bootstrap support and pinned baseline |
| Nodian | Keeps paired relationship inverses synchronized |
| Breadcrumbs | Semantic relationship navigation, matrix/tree, graph/canvas creation |
| Dataview | Dashboards, model-health and traceability queries |
| Fileclass | Typed property/schema editing support |
| Advanced Canvas | Architecture and relationship visualization |
| Templater | ID generation, folder-driven element templates |
| QuickAdd | Optional fast creation/automation launcher |
| Table Exporter | Export query tables for reviews and engineering handoffs |
| Obsidian Git | Git pull/commit/push workflow for collaborative vault synchronization; not required for MDSE semantics |

Core Obsidian `Canvas`, `Properties`, `Bases`, `Graph`, backlinks, and templates are also enabled.

## First open

1. Open this folder as an Obsidian vault.
2. If Obsidian asks about Restricted Mode/community plugins, enable the trusted bundled plugins.
3. Run **Nodian: Full sync** once after first open or after bulk imports.
4. Run **Breadcrumbs: Rebuild Graph** after bulk relationship changes.
5. Open `00_Home/MDSE Home.md`.

No API key or cloud service is required for the MDSE core experience. QuickAdd online features are disabled.

Obsidian Git is included as a repository synchronization convenience. Its automatic commit/pull/push timers are disabled by default so repository synchronization remains explicit.
