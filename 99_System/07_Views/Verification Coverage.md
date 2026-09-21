# Verification Coverage

```dataview
TABLE verifiedBy, satisfiedBy, appliesTo
FROM "40_Requirements"
WHERE type = "Requirement"
SORT file.name ASC
```

## Verification library

```dataview
TABLE kind, verifies, appliesTo, startState, operatingState, endState
FROM "60_Verification/02_Verifications"
WHERE type = "Verification"
SORT file.name ASC
```
