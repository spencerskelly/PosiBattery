# Open Issues

```dataview
TABLE kind, affects, causes, status
FROM "51_Issues"
WHERE type = "Issue" AND status != "Retired"
SORT file.name ASC
```
