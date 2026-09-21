# Model Dashboard

```dataviewjs
const pages=dv.pages('""').where(p=>p.id&&p.type);
const byType={}; const byStatus={};
for(const p of pages){byType[p.type]=(byType[p.type]||0)+1; byStatus[p.status||"(none)"]=(byStatus[p.status||"(none)"]||0)+1;}
dv.header(2,"Elements by type"); dv.table(["Type","Count"],Object.entries(byType).sort());
dv.header(2,"Lifecycle"); dv.table(["Status","Count"],Object.entries(byStatus).sort());
```
