# MDSE Home

This is a clean, domain-neutral MDSE starter vault. Start with the governing rules, then use the generic examples to understand the mechanics before building the project model.

## Start here

1. [[99_System/10_Docs/MDSE Modeling Ruleset 1.18|MDSE Modeling Ruleset 1.18]]
2. [[99_System/10_Docs/MDSE Metamodel|MDSE Metamodel]]
3. [[99_System/10_Docs/Relationship Ownership|Relationship Ownership]]
4. [[99_System/10_Docs/Model Evidence and Acceptance Standard|Model Evidence and Acceptance Standard]]
5. [[99_System/10_Docs/Function Ownership and Interaction Standard|Function Ownership and Interaction Standard]]
6. [[99_System/10_Docs/Stakeholder Journey Modeling Standard|Stakeholder Journey Modeling Standard]]
7. [[99_System/10_Docs/Folder Navigation and View Standard|Folder Navigation and View Standard]]
8. [[99_System/02_AI/AI_INSTRUCTIONS|AI Instructions]]

## Recommended first modeling pass

- define system/product boundary and control classification;
- identify reusable Actors and stakeholder journeys;
- identify external goals / Use Cases;
- identify controlled Functions and performers;
- capture concrete Interfaces and Item Flows;
- capture Requirements and their evidence/basis;
- identify Designs/decisions and unresolved hypotheses;
- add Contexts, States, State Machines, and Transitions where behavior depends on them;
- identify Failure Modes / Issues / risks;
- outline Verification strategy and gaps.

Do not create every element type for completeness. Missing information should remain visible as a question or model check.

## AI-assisted start

Use `90_Concept/AI_Workspace` for broad AI-generated coverage before team discussion. AI should preserve evidence, uncertainty, and questions rather than forcing a complete-looking model.

## Model snapshot

```dataviewjs
const pages = dv.pages('""').where(p => p.id && p.type);
const counts = {}; for (const p of pages) counts[p.type]=(counts[p.type]||0)+1;
dv.table(["Type","Count"], Object.entries(counts).sort((a,b)=>a[0].localeCompare(b[0])));
```
