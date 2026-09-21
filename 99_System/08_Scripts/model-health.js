const MODEL_ROOTS = ["10_Things","20_Interfaces","21_Item_Flows","25_Contexts","30_Functions","31_Functional_Flows","35_States","36_State_Machines","37_Transitions","40_Requirements","41_Designs","45_Use_Cases","47_Actors","50_Failure_Modes","51_Issues","55_Info","60_Verification","70_Documents","71_Artifacts"];
const statuses=new Set(["Draft","Review","Approved","Deprecated","Retired"]);
const controls=new Set(["controlled","modifiable","contextual","reference"]);
const kindMap={
"Thing":["electrical","circuit","mechanical","software","firmware"],"Interface":["electrical & material","data","mechanical","generic physical","environmental"],"Item Flow":["information","energy","material"],"Function":["system","hardware","software","module"],"Requirement":["functional","design","standard","stakeholder"],"Design":["characteristic","decision"],"Use Case":["what","where","why","when"],"Issue":["engineering issue","lifecycle risk"],"Info":["need","objective","concern","decision","assumption","rationale","finding","analysis","trade study","calculation","milestone","lesson learned"],"Verification":["test","analysis","inspection","demonstration"],"Procedure":["test","assembly","configuration","commissioning","calibration","maintenance","repair","decommissioning"],"Document":["standard","specification","report","drawing"],"Artifact":["image","document"]};
const rels = ["conflictsWith", "addressedBy", "addresses", "affectedBy", "affects", "applies", "appliesTo", "behaviorOf", "carries", "causedBy", "causes", "connectedBy", "connects", "contextOf", "dependencyOf", "dependsOn", "derivedBy", "derivedFrom", "describedBy", "describes", "designOf", "dut", "endState", "endStateOf", "equipmentUsed", "evidenceFor", "exercisedBy", "exercises", "finalState", "flowsOn", "hasBehavior", "hasContext", "hasDesign", "hasEvidence", "hasInstance", "hasOption", "hasPart", "hasParticipant", "hasResult", "hasState", "hasStateMachine", "hasTransition", "initialState", "instanceOf", "operatingState", "operatingStateOf", "optionOf", "partOf", "participatesIn", "performedBy", "performs", "plannedDUTs", "providesEnvironment", "providesFixture", "providesInterfaceEquipment", "providesLoad", "providesMeter", "providesSource", "realizedBy", "realizes", "requiresEnvironment", "requiresFixture", "requiresInterfaceEquipment", "requiresLoad", "requiresMeter", "requiresSource", "resultOf", "satisfiedBy", "satisfies", "scopeRequirements", "sequence", "source", "sourceOf", "startState", "startStateOf", "stateMachineOf", "stateOf", "subject", "subjectOf", "subtypeOf", "supersededBy", "supersedes", "supertypeOf", "target", "targetOf", "tracesFrom", "tracesTo", "transitionOf", "trigger", "usedByPlan", "usesSetup", "verifiedBy", "verifies"];
const pages=dv.pages('""').where(p=>p.file && MODEL_ROOTS.some(r=>p.file.path.startsWith(r+"/")));
const issues=[]; const idOwners=new Map(); const formerOwners=new Map();
const relationshipPairs=[
["subtypeOf","supertypeOf"],["hasPart","partOf"],["dependsOn","dependencyOf"],["derivedFrom","derivedBy"],
["supersedes","supersededBy"],["describes","describedBy"],["tracesTo","tracesFrom"],["instanceOf","hasInstance"],
["performs","performedBy"],["hasDesign","designOf"],["hasStateMachine","stateMachineOf"],["hasContext","contextOf"],
["hasBehavior","behaviorOf"],["appliesTo","applies"],["satisfies","satisfiedBy"],["verifies","verifiedBy"],
["subject","subjectOf"],["hasParticipant","participatesIn"],["realizedBy","realizes"],["optionOf","hasOption"],
["connects","connectedBy"],["carries","flowsOn"],["source","sourceOf"],["target","targetOf"],
["hasState","stateOf"],["hasTransition","transitionOf"],["startState","startStateOf"],["endState","endStateOf"],
["operatingState","operatingStateOf"],["exercises","exercisedBy"],["addresses","addressedBy"],["affects","affectedBy"],
["causes","causedBy"],["usesSetup","usedByPlan"],["resultOf","hasResult"],["hasEvidence","evidenceFor"],["conflictsWith","conflictsWith"]
];
function add(level,code,p,msg){issues.push([level,code,p.file.link,msg]);}
function arr(v){if(v==null)return[]; return Array.isArray(v)?v:[v];}
for(const p of pages){
 if(!p.id) add("ERROR","MISSING-ID",p,"Modeled note has no id");
 if(!p.type) add("ERROR","MISSING-TYPE",p,"Modeled note has no type");
 if(p.id){if(idOwners.has(p.id)) add("ERROR","DUPLICATE-ID",p,`Also used by ${idOwners.get(p.id)}`); else idOwners.set(p.id,p.file.path); if(!p.file.name.startsWith(p.id+" - ")) add("WARN","FILENAME-ID",p,"Filename does not start with the stable ID");}
 if(p.status && !statuses.has(String(p.status))) add("WARN","STATUS-VALUE",p,`Unrecognized status: ${p.status}`);
 if(p.control && !controls.has(String(p.control))) add("WARN","CONTROL-VALUE",p,`Unrecognized control: ${p.control}`);
 for(const old of arr(p.formerIds)){const k=String(old); if(!k)continue; if(idOwners.has(k)||formerOwners.has(k)) add("ERROR","FORMER-ID-COLLISION",p,`formerId ${k} is already used`); else formerOwners.set(k,p.file.path);}
 if(kindMap[p.type] && p.kind && !kindMap[p.type].includes(String(p.kind))) add("WARN","KIND-VALUE",p,`Unexpected kind '${p.kind}' for ${p.type}`);
 if(p.type==="Failure Mode"){const vals=[p.severity,p.occurrence,p.detection].filter(v=>v!=null&&v!==""); if(vals.length>0&&vals.length<3)add("WARN","PARTIAL-FMEA",p,"FMEA rating set is incomplete"); for(const v of vals)if(Number(v)<1||Number(v)>10)add("ERROR","FMEA-RANGE",p,"FMEA ratings must be 1–10");}
 if(arr(p.tracesTo).length)add("WARN","WEAK-TRACE",p,"tracesTo is a migration escape hatch; classify it into a stronger semantic relationship when possible");
 if(arr(p.satisfies).length && !["Function","Design"].includes(p.type)) add("ERROR","SATISFY-SOURCE",p,"Only Function or Design should author satisfies");
 if(arr(p.verifies).length && p.type!=="Verification") add("ERROR","VERIFY-SOURCE",p,"Only Verification should author verifies");
 for(const r of rels){for(const x of arr(p[r])){let path=null; if(x?.path) path=x.path; else {const s=String(x); const m=s.match(/\[\[([^\]|#]+)(?:[|#][^\]]*)?\]\]/); path=m?m[1]:null;} if(path && !dv.page(path)) add("WARN","UNRESOLVED-LINK",p,`${r}: ${path}`);}}
}

for(const p of pages){
 for(const [forward,inverse] of relationshipPairs){
  for(const x of arr(p[forward])){
   let target=null;
   if(x?.path) target=dv.page(x.path); else {const raw=String(x); const mm=raw.match(/\[\[([^\]|#]+)(?:[|#][^\]]*)?\]\]/); if(mm) target=dv.page(mm[1]);}
   if(!target) continue;
   const sourceName=p.file.name;
   const hasInverse=arr(target[inverse]).some(v=>{
    const raw=v?.path?v.path:String(v);
    const mm=raw.match(/\[\[([^\]|#]+)(?:[|#][^\]]*)?\]\]/);
    const path=mm?mm[1]:raw;
    return String(path).split("/").pop()===sourceName;
   });
   if(!hasInverse) add("WARN","MISSING-INVERSE",p,forward+" -> "+target.file.name+" is missing "+inverse+" backlink");
  }
 }
}
issues.sort((a,b)=>(a[0]===b[0]?String(a[1]).localeCompare(String(b[1])):(a[0]==="ERROR"?-1:1)));
dv.paragraph(`Checked ${pages.length} modeled notes. ${issues.filter(x=>x[0]==="ERROR").length} errors, ${issues.filter(x=>x[0]==="WARN").length} warnings.`);
dv.table(["Level","Code","Note","Finding"],issues);
