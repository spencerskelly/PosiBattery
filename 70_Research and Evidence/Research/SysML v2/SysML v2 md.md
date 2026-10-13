I would create a reference called “SysML v2 in Markdown: Authoring and Tooling Profile.”

Its central rule would be: Markdown is the document container; SysML v2 is the modeling language. The Obsidian plugin connects the two—it should not invent a competing modeling language.

The complexity is manageable if you keep that boundary clear. Extracting code blocks and associating elements with notes is relatively straightforward. Resolving model references, inheritance, ports, flows, and behavior is a language-tooling problem and should be delegated to a SysML-capable engine.

The most important word in the methodology is **ownership**: which file owns a declaration, which namespace owns an element, and which source owns each editable fact.

## 1. Work backward from how SysML v2 actually works

SysML v2 has textual syntax, but its meaning is not just the text’s indentation or nesting. It builds on KerML, with model elements, namespaces, memberships, definitions, usages, and semantic relationships. Packages organize names and visibility; imports participate in name resolution.[[dvcon-proceedings](https://dvcon-proceedings.org/wp-content/uploads/SysML-v2-An-Overview-with-SysMD-Demonstration.pdf)][[incose](https://www.incose.org/wp-content/uploads/legacy/content-library/moving_forward_with_sysml_v2-incose_atlanta_chapter-sfriedenthal-2024-07-17.pdf?sfvrsn=e5548c7_2)]

For your plugin, I would separate five stages:

```
Markdown document
        ↓ extract
SysML source text
        ↓ parse
Syntax tree
        ↓ resolve names and semantics
Semantic model
        ↓ project
Obsidian relationships, tables, diagrams, and navigation
```

Each stage answers a different question.

|Stage|Question it answers|Example|
|---|---|---|
|Extraction|Where is the model text?|Lines inside a `sysml` fence|
|Parsing|What did the author declare?|A part usage named `controller`|
|Name resolution|Which element does a reference mean?|Which `Controller` definition types that usage?|
|Semantic analysis|How does the declaration participate in the model?|Ownership, typing, specialization, inherited features|
|Projection|How should a user see it?|“Has part,” “Typed by,” or a port connection view|

A parser alone does not provide the entire semantic model. Existing SysML tooling distinguishes parsing, symbol infrastructure, well-formedness checks, and language-server functionality such as diagnostics and completion.[[github](https://github.com/MontiCore/sysmlv2)]

### Definitions and usages change the navigation model

Consider:

```
package Charging {
    part def Controller;

    part def Charger {
        part controller : Controller;
    }
}
```

There are at least three distinct elements:

```
Charging::Controller
    reusable definition

Charging::Charger
    reusable assembly definition

Charging::Charger::controller
    usage owned by the assembly definition
```

The usage has an owning context and a type. Definitions and usages form a consistent pattern across SysML v2, including parts, actions, and requirements.[[incose](https://www.incose.org/wp-content/uploads/legacy/content-library/moving_forward_with_sysml_v2-incose_atlanta_chapter-sfriedenthal-2024-07-17.pdf?sfvrsn=e5548c7_2)]

Consequently, an Obsidian graph should not collapse these into:

```
Charger → Controller
```

That loses the usage—the specific role of the controller within the charger.

A better projection is:

```
Charger
    └── owns usage: controller
                       └── typed by: Controller
```

You can simplify the presentation, but the underlying index should retain the distinction.

### Namespaces are not folders

SysML name resolution uses model namespaces and imports. It is not based on Markdown file paths. A qualified reference such as `Charging::Controller` identifies a model element, not a file.[[dvcon-proceedings](https://dvcon-proceedings.org/wp-content/uploads/SysML-v2-An-Overview-with-SysMD-Demonstration.pdf)]

Therefore:

- Moving a note should not move its model element to another namespace.
- Renaming a note should not automatically rename a declaration.
- An Obsidian wikilink should not substitute for a SysML reference.
- A model rename should be an explicit refactoring operation.

This separation is essential for a vault that will evolve over years.

## 2. How complex would the Obsidian rules be?

I would keep the document rules small and let the model rules remain SysML’s responsibility.

|Capability|Proposed complexity|Reason|
|---|---|---|
|Recognize model notes|Low|A small frontmatter contract|
|Extract fenced SysML|Low–moderate|Must respect Markdown fences and preserve source positions|
|Show declarations in an outline|Moderate|Requires parsing and source mapping|
|Resolve references across notes|High without an engine; moderate integration with one|Requires workspace-wide name resolution|
|Show inherited ports and features|High semantic dependency|Text scanning is insufficient|
|Generate relationship views|Moderate after semantic analysis|Requires carefully defined projections|
|Edit diagrams and write back to source|High|Requires source-preserving transformations|
|Validate state behavior structurally|High semantic dependency|More than identifying state names|
|Simulate behavior|Separate, substantially larger scope|Execution is not the same as parsing or validation|
|Synchronize with a model repository|High|Identity, revisions, ownership, and conflict handling|

These are qualitative engineering estimates, not measured implementation effort.

My first version would support read-only derived views and direct text editing. I would defer editable diagrams, arbitrary multi-note declaration fragments, repository synchronization, and simulation.

Existing language-server implementations provide a useful starting point for editor integration, but capability and language-version compatibility would need qualification against your reference models.[[github](https://github.com/MontiCore/sysmlv2)][[github](https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/issues/571)]

## 3. The authoring methodology I would choose

I would call the approach “literate SysML”: formal model content lives alongside the rationale, decisions, issues, and explanation that make it understandable.

### Rule 1: Three kinds of information, with explicit authority

|Information|Authoritative location|Examples|
|---|---|---|
|Formal model|SysML block|Parts, ports, values, connections, flows, states|
|Document workflow|YAML frontmatter|Owner, review status, note ID|
|Engineering narrative|Markdown body|Rationale, assumptions, alternatives, unresolved questions|

Do not store an editable model fact in two layers.

For example, if a port is declared in SysML:

```
port batteryCommunication : BatteryCommunicationPort;
```

do not also maintain an independently editable YAML list of the assembly’s ports.

A generated property can be useful for filtering, but it must be identified as derived, with a defined refresh and staleness policy.

### Rule 2: A note owns a complete source unit

For the initial profile, I would require:

- Exactly one authoritative `sysml` block in each model note.
- Complete declarations inside that block.
- Explicit namespace structure in the source.
- No implicit wrapping based on folder names.
- No declaration beginning in one note and ending in another.

This is deliberately restrictive. It means extracted source can be inspected and validated outside Obsidian without reconstructing hidden authoring conventions.

Other code blocks may contain examples, but they should use a different fence label, such as `sysml-example`, and must not enter the workspace.

### Rule 3: One primary subject per note—not necessarily one element

For your atomic-note approach, I would make the atomic unit an engineering subject, not every syntactic declaration.

Examples:

|Note subject|Reasonable contents|
|---|---|
|Temperature sensor definition|Definition, ports, attributes|
|Charger assembly|Part definition, internal usages, connections, flows|
|Operating lifecycle|A reusable state definition and related behavior declarations|
|Installation context|External participants and connections|
|Requirement|Requirement definition or usage, according to the selected modeling pattern|

A complex assembly can own dozens of nested usages and relationships while remaining one coherent note.

Creating a note for every port, transition, or anonymous relationship would likely make authorship and navigation harder rather than clearer.

### Rule 4: Extracted source must remain portable

The exporter should produce ordinary `.sysml` source files from the authoritative fences, preserving their text.

It should not require Obsidian-specific syntax inside those blocks.

This gives you a practical portability test:

> Can the exported workspace be opened and checked by the selected SysML tool without the Obsidian plugin?

That is stronger than merely saying the vault “supports SysML.”

## 4. A minimal reference note

This is the document contract I would standardize first:

````
---
note_id: NOTE-000214
document_kind: model
primary_symbol: Charging::Charger
review_status: draft
owner: Hardware Engineering
---

# Charger

## Purpose

Provide controlled battery charging and coordinate the internal
power converter and supervisory controller.

## Model

```sysml
package Charging {

    part def Charger {
        part controller : Charging::Controller;
        part converter : Charging::PowerConverter;
    }
}
```

## Rationale

The controller is separated from the power converter so that
control electronics can evolve independently of the power stage.

## Open questions

- Should converter diagnostics be modeled as a separate interface?
- Which functions remain available while the power stage is disabled?

## Related information

- [[Power Stage Trade Study]]
- [[Controller Architecture Decision]]
````

Here:

- `note_id` identifies the document.
- `primary_symbol` selects the subject for the plugin’s default view.
- The SysML declaration determines namespace and model ownership.
- The YAML does not determine the assembly’s parts.
- Wikilinks provide document navigation, not formal model relationships.

The references to `Controller` and `PowerConverter` must resolve in the extracted workspace. Until they do, the plugin should report unresolved references rather than guess.

## 5. The hardest methodology decision: splitting assemblies and behavior

My previous example put structure and an exhibited state machine into one declaration. That is useful for illustration, but it can become unwieldy.

I would support two initial patterns.

### Pattern A: Cohesive assembly note

Keep the assembly’s internal usages, connections, selected flows, and local state behavior together.

Use this when:

- The model is small enough to review as a unit.
- The behavior is specific to that assembly.
- Splitting would introduce more cross-references than clarity.

### Pattern B: Reusable definitions in separate notes

Place reusable part, port, item, action, and state definitions in their own notes. The assembly references or uses them.

Use this when:

- Multiple products share the definitions.
- Different teams own structure and behavior.
- The behavior has a substantial independent lifecycle.

The definition/usage pattern supports this separation conceptually; the exact declarations must be checked against the chosen SysML implementation and modeling conventions.[[incose](https://www.incose.org/wp-content/uploads/legacy/content-library/moving_forward_with_sysml_v2-incose_atlanta_chapter-sfriedenthal-2024-07-17.pdf?sfvrsn=e5548c7_2)]

I would not initially support “append these members to an existing definition from another Markdown note.”

That is a custom composition facility, not just Markdown extraction. It would require rules for ordering, namespace context, duplicate members, source ownership, and write-back. If you later need it, specify it as an explicit extension and test it separately.

## 6. Ports and flows need a modeling convention, not just syntax

Your reference should distinguish four concepts:

|Concept|Question|
|---|---|
|Port|Where may the component interact?|
|Connection|Which endpoints are related?|
|Flow|What transfer is modeled, and in which direction?|
|Binding|Which features are equated?|

The earlier worked example used these distinctions, but I would not adopt that example as normative without validating it.

In particular, I would revise the reference to require:

1. Direction is stated relative to the owning part.
2. Conjugated port usage is explained consistently.
3. Boundary delegation is distinguished from internal connectivity.
4. Payloads have explicit types where needed.
5. Physical topology and information transfer are separate.
6. Bidirectional interfaces are not reduced to one directional flow.
7. A binding is not treated as a generic “wire.”
8. Electrical ground, signal reference, and protective-earth bonding have distinct domain meanings.

The binding, conjugation, and connection syntax has defined language meaning; the electrical interpretation is an additional engineering convention your methodology must document.[[rickymillar.github](https://rickymillar.github.io/sysmlv2-book/ch06-connections-and-interfaces.html)][[rickymillar.github](https://rickymillar.github.io/sysmlv2-book/appendix-a-syntax-reference.html)]

For your power/signal/ground relationship views, I would display human-readable labels while retaining the formal relationship and domain classification underneath. “Supplies power to” should be a qualified view of modeled information—not a replacement for the underlying semantics.

## 7. Identity and source mapping deserve their own specification

There are three different identities to manage:

|Identity|Purpose|
|---|---|
|Document ID|Survives Markdown file moves and renames|
|Model address|Finds a declaration through its namespace and name|
|Persistent element identity|Tracks an element across model renames and restructuring|

A qualified name is an address, not necessarily a stable identity.

For the first version, I would use:

- Stable note IDs.
- Qualified names for semantic lookup.
- Source locations for click-through.
- Explicit rename operations for tracked refactoring.

I would not promise stable identity for every nested element across arbitrary manual text edits.

Before adding repository synchronization or long-lived per-element annotations, choose a persistent identity strategy: supported model metadata, a managed sidecar registry, or repository-owned IDs. Evaluate it against the selected engine; do not invent a pseudo-SysML identifier annotation and assume external tools will recognize it.

The source map should record:

```
Model element
    → extracted source file
    → originating note ID
    → fenced block
    → declaration source range
```

That supports diagnostics, navigation, and safe edits.

## 8. Validation should expose several different levels of confidence

I would define five gates.

|Gate|What passes|
|---|---|
|Document validation|Frontmatter and authoritative block follow the Markdown profile|
|Syntax validation|SysML source parses|
|Workspace validation|References and imports resolve|
|Semantic validation|Supported language checks pass|
|Engineering review|The model meets project conventions and has reviewed meaning|

A model can pass one gate and fail another.

Examples:

- A state machine can parse but reference an undefined event type.
- A flow can resolve but violate a project interface convention.
- A satisfaction assertion can be structurally valid without demonstrating that a design meets the requirement.
- A connected interface can still omit timeout or failure behavior.

Existing language tooling provides parsing and well-formedness infrastructure, but engineering adequacy remains a separate concern.[[github](https://github.com/MontiCore/sysmlv2)]

### Incomplete typing must be allowed

The methodology should explicitly allow draft source to be incomplete.

The plugin should:

- Show current diagnostics.
- Keep prose editing available.
- Distinguish current parsed information from stale last-valid information.
- Exclude stale or invalid projections from approved baselines.
- Never silently promote prose into formal assertions.

## 9. What I would create as the actual reference

I would build a versioned reference vault plus an implementation-neutral specification.

The vault teaches the method; the specification tells developers exactly what the plugin must do.

|Reference artifact|Contents|
|---|---|
|`00 — Overview`|Goals, scope, terminology, supported language/tool versions|
|`01 — Normative Markdown Profile`|Required fields, fence rules, authority, extraction|
|`02 — Workspace and Namespaces`|Source discovery, imports, libraries, scope, export|
|`03 — Identity and Ownership`|Note IDs, element addresses, source ownership, rename policy|
|`04 — Modeling Conventions`|Definitions/usages, assemblies, ports, connections, flows, behavior|
|`05 — Relationship Projection Catalog`|Formal concept → user-facing labels → navigation behavior|
|`06 — Validation and Diagnostics`|Error levels, incomplete editing, staleness, release gates|
|`07 — Plugin Integration Contract`|Engine interface, source maps, indexing, edits|
|`08 — Authoring Templates`|Copyable note templates|
|`09 — Worked Reference Models`|Increasingly complex, engine-validated examples|
|`10 — Conformance Tests`|Expected extraction, diagnostics, symbols, and views|
|`11 — Change and Baseline Management`|Reviews, migrations, export manifests, version policy|

### Make the normative rules testable

Use requirement-style statements, for example:

```
MDV2-001
A model note MUST contain exactly one authoritative sysml fence.

MDV2-002
The extractor MUST preserve the source text inside the fence,
apart from explicitly documented newline normalization.

MDV2-003
A file move MUST NOT change the extracted model namespace.

MDV2-004
Ordinary Markdown links MUST NOT create formal model relationships.

MDV2-005
Every displayed model relationship MUST identify its semantic kind
and its originating declaration or derivation.

MDV2-006
Derived information MUST NOT become an independent editable authority.

MDV2-007
Diagnostics MUST map back to the originating Markdown source range.

MDV2-008
The plugin MUST distinguish authored relationships from inherited,
derived, suggested, or stale information.
```

These are proposed profile requirements, not existing SysML requirements.

## 10. The reference models are as important as the prose

I would include a small progression:

|Model|What it proves|
|---|---|
|One part definition|Basic extraction and navigation|
|Definition plus usage|Ownership versus typing|
|Two notes with references|Workspace name resolution|
|Shared library plus product model|Imports and reuse|
|Assembly with internal ports|Nested declarations and boundary navigation|
|Connections and opposite-direction flows|Topology versus transfer|
|State machine|Triggers, guards, state actions, diagnostics|
|Specialization and inherited features|Derived model views|
|Broken references and incomplete syntax|Safe failure behavior|
|Rename and move scenarios|Identity and refactoring boundaries|

Each model should ship with expected results:

```
Source notes
Expected extracted .sysml files
Expected declared symbols
Expected resolved references
Expected diagnostics
Expected relationship projections
```

The tests should compare normalized semantics—not just screenshots or generated text.

I would also record the exact engine and library versions used to validate each reference model.

## 11. Implementation boundaries I would enforce

The plugin should own:

- Markdown extraction.
- Note identity.
- Source mapping.
- Obsidian navigation.
- Presentation and relationship labels.
- Document workflow.
- Safe integration with the editor.

The SysML engine should own:

- Parsing.
- Name resolution.
- Supported semantic checks.
- Inheritance and specialization interpretation.
- Model-level queries.

For file changes, follow Obsidian’s documented editing rules: use the Editor API for active notes, atomic `Vault.process` for background changes, and `processFrontMatter` for frontmatter modifications.[[docs.obsidian](https://docs.obsidian.md/Plugins/Releasing/Plugin+guidelines)]

I would make diagram editing a later capability because it adds another hard requirement: modifying a model must preserve users’ surrounding prose, comments, formatting, and concurrent edits.

## Recommended starting scope

For your vault, I would begin with complete SysML blocks, explicit namespaces, reusable definitions in separate notes, and assembly-level notes containing their internal usages.

The first reference should prove four things:

1. Extracted source is valid in the selected SysML tool.
2. Formal relationships can drive readable Obsidian views.
3. Users can freely edit rationale and incomplete drafts.
4. Moving or reorganizing documents does not silently change the model.

That produces a methodology you can actually qualify and maintain—not just a collection of Markdown templates that look like SysML.