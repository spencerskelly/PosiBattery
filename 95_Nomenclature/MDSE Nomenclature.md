# MDSE Nomenclature

Use the exact type, kind, and relationship names from the system schema. This note is a quick human index; the machine-readable authority is in `99_System/03_Schemas`.

## Type vocabulary

- **Thing** — `THG`
- **Interface** — `INT`
- **Item Flow** — `IFLOW`
- **Context** — `CTX`
- **Function** — `FUNC`
- **Functional Flow** — `FFLOW`
- **State** — `STATE`
- **State Machine** — `SM`
- **Transition** — `TRANS`
- **Requirement** — `REQ`
- **Design** — `DES`
- **Use Case** — `UC`
- **Actor** — `ACT`
- **Failure Mode** — `FM`
- **Issue** — `ISS`
- **Info** — `INFO`
- **Step** — `STEP`
- **Verification** — `VER`
- **Procedure** — `PROC`
- **Setup** — `SETUP`
- **Plan** — `PLAN`
- **Result** — `RES`
- **Document** — `DOC`
- **Artifact** — `ART`

## High-value semantic distinctions

- `subtypeOf` = **is a kind of**.
- `hasPart` = **is composed/decomposed into**.
- `dependsOn` = real prerequisite/reliance, never mere sequence.
- `appliesTo` = requirement/verification/failure-mode scope.
- `satisfies` = fulfillment by Function/Design only.
- `verifies` = verification evidence intent against Requirement.
- `describes` = definition/explanation, not fulfillment.
- `source`/`target` = direction for Item Flow or Transition.
