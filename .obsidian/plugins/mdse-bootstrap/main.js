const { Plugin, Notice, requestUrl } = require("obsidian");

const PINNED = [
  { id: "breadcrumbs",      repo: "michaelpporter/breadcrumbs",                version: "4.21.11" },
  { id: "dataview",         repo: "blacksmithgu/obsidian-dataview",           version: "0.5.68" },
  { id: "nodian",           repo: "AkiSantin/Nodian",                         version: "1.4.14" },
  { id: "fileclass",        repo: "mdelobelle/fileclass",                     version: "0.2.15" },
  { id: "advanced-canvas",  repo: "Developer-Mike/obsidian-advanced-canvas",  version: "7.0.0" },
  { id: "table-exporter",   repo: "wikty/obsidian-table-exporter",            version: "0.3.0" },
  { id: "templater-obsidian", repo: "SilentVoid13/Templater",                 version: "2.25.0" },
  { id: "quickadd",         repo: "chhoumann/quickadd",                       version: "2.23.0" }
];

function cleanVersion(v) { return String(v || "").replace(/^v/i, ""); }

module.exports = class MDSEBootstrap extends Plugin {
  async onload() {
    this.running = false;
    this.addCommand({ id: "repair-plugin-stack", name: "Repair / reinstall pinned plugin stack", callback: () => this.bootstrap(true) });
    this.addCommand({ id: "repair-model-relationships", name: "Repair relationship inverses and Canvas edges", callback: () => this.repairRelationshipsAndCanvases(true) });
    this.app.workspace.onLayoutReady(() => { void (async () => { await this.bootstrap(false); window.setTimeout(() => { void this.repairRelationshipsAndCanvases(false); }, 3500); })(); });
  }

  async bootstrap(force) {
    if (this.running) return;
    this.running = true;
    try {
      const state = (await this.loadData()) || {};
      const healthy = await this.stackIsPresent();
      if (!force && state.completed && healthy) return;

      new Notice("MDSE: preparing the plugin stack…", 5000);
      const installed = [];
      for (const p of PINNED) {
        const changed = await this.ensurePlugin(p, force);
        installed.push(`${p.id} ${p.version}${changed ? " installed" : " ready"}`);
      }

      // Ask Obsidian to discover and enable the plugins immediately when its internal plugin manager is available.
      let immediate = false;
      const manager = this.app.plugins;
      if (manager && typeof manager.loadManifests === "function" && typeof manager.enablePluginAndSave === "function") {
        try {
          await manager.loadManifests();
          for (const p of PINNED) await manager.enablePluginAndSave(p.id);
          immediate = true;
        } catch (e) {
          console.warn("MDSE Bootstrap: immediate enable failed; reload fallback will be used", e);
        }
      }

      // Guaranteed reload fallback: Obsidian reads this file at startup.
      const enabled = ["mdse-bootstrap", ...PINNED.map(p => p.id)];
      const configDir = this.app.vault.configDir || ".obsidian";
      await this.app.vault.adapter.write(`${configDir}/community-plugins.json`, JSON.stringify(enabled, null, 2) + "\n");

      await this.saveData({ completed: true, completedAt: new Date().toISOString(), versions: Object.fromEntries(PINNED.map(p => [p.id, p.version])) });
      await this.writeStatus(installed, immediate);
      new Notice(immediate ? "MDSE: plugin stack is ready." : "MDSE: plugin stack installed. Reload Obsidian once to enable it.", 12000);
    } catch (e) {
      console.error("MDSE Bootstrap failed", e);
      new Notice(`MDSE bootstrap failed: ${e?.message || e}. Check internet access, then run “MDSE Bootstrap: Repair / reinstall pinned plugin stack”.`, 15000);
      await this.writeStatus([`ERROR: ${e?.message || e}`], false);
    } finally {
      this.running = false;
    }
  }

  async repairRelationshipsAndCanvases(notify = false) {
    try {
      const commandId = "nodian:sync-all-bidirectional-relations";
      const command = this.app.commands?.commands?.[commandId];
      if (command) await this.app.commands.executeCommandById(commandId);
      else console.warn("MDSE Bootstrap: Nodian full-sync command is not available yet.");
      const changed = await this.refreshCanvasRelationshipEdges();
      if (notify) new Notice("MDSE: relationship repair complete; " + changed + " Canvas file(s) updated.", 8000);
    } catch (e) {
      console.error("MDSE relationship repair failed", e);
      if (notify) new Notice("MDSE relationship repair failed: " + (e?.message || e), 10000);
    }
  }

  relationshipFields() {
    return ["subtypeOf","hasPart","dependsOn","derivedFrom","supersedes","describes","tracesTo","instanceOf","performs","hasDesign","hasStateMachine","hasContext","hasBehavior","appliesTo","satisfies","verifies","subject","hasParticipant","realizedBy","optionOf","connects","carries","source","target","hasState","hasTransition","startState","endState","operatingState","exercises","addresses","affects","causes","usesSetup","resultOf","hasEvidence","conflictsWith"];
  }

  linkTargets(value) {
    const vals = Array.isArray(value) ? value : (value == null ? [] : [value]);
    const out = [];
    for (const v of vals) {
      if (typeof v !== "string") continue;
      const mm = v.match(/^\[\[([^\]|#]+)(?:[|#][^\]]*)?\]\]$/);
      if (mm) out.push(mm[1].trim());
    }
    return out;
  }

  async refreshCanvasRelationshipEdges() {
    const fields = new Set(this.relationshipFields());
    const canvases = this.app.vault.getFiles().filter(f => f.extension === "canvas");
    let changedCount = 0;
    for (const file of canvases) {
      let doc;
      try { doc = JSON.parse(await this.app.vault.cachedRead(file)); } catch (_) { continue; }
      if (!Array.isArray(doc.nodes) || !Array.isArray(doc.edges)) continue;
      const fileNodes = new Map();
      for (const node of doc.nodes) {
        if (node?.type !== "file" || typeof node.file !== "string" || !node.file.endsWith(".md")) continue;
        let target = this.app.vault.getAbstractFileByPath(node.file);
        if (!target) {
          const basename = node.file.split("/").pop();
          const matches = this.app.vault.getMarkdownFiles().filter(f => f.name === basename);
          if (matches.length === 1) { target = matches[0]; node.file = target.path; }
        }
        if (target) fileNodes.set(target.path, node);
      }
      if (fileNodes.size < 2) continue;
      const relationEdges = [], seen = new Set();
      for (const [path, node] of fileNodes) {
        const mdFile = this.app.vault.getAbstractFileByPath(path);
        const fm = this.app.metadataCache.getFileCache(mdFile)?.frontmatter;
        if (!fm) continue;
        for (const field of fields) {
          for (const rawTarget of this.linkTargets(fm[field])) {
            const targetFile = this.app.metadataCache.getFirstLinkpathDest(rawTarget, path);
            if (!targetFile) continue;
            const targetNode = fileNodes.get(targetFile.path);
            if (!targetNode) continue;
            const a=node.id, b=targetNode.id;
            const key = field === "conflictsWith" ? field + "|" + [a,b].sort().join("|") : field + "|" + a + "|" + b;
            if (seen.has(key)) continue;
            seen.add(key);
            relationEdges.push({id:"mdse-"+field+"-"+a+"-"+b,fromNode:a,toNode:b,label:field});
          }
        }
      }
      const manual = doc.edges.filter(e => !String(e.id || "").startsWith("mdse-"));
      for (const rel of relationEdges) {
        const existing = manual.find(e => e.fromNode === rel.fromNode && e.toNode === rel.toNode);
        if (existing && !existing.label) existing.label = rel.label;
      }
      const auto = relationEdges.filter(rel => !manual.some(e => e.fromNode === rel.fromNode && e.toNode === rel.toNode && e.label === rel.label));
      const next = {...doc, edges:[...manual,...auto]};
      const text = JSON.stringify(next,null,2), current = JSON.stringify(doc,null,2);
      if (text !== current) { await this.app.vault.modify(file,text); changedCount++; }
    }
    return changedCount;
  }

  async stackIsPresent() {
    const configDir = this.app.vault.configDir || ".obsidian";
    for (const p of PINNED) {
      const base = `${configDir}/plugins/${p.id}`;
      if (!(await this.app.vault.adapter.exists(`${base}/main.js`)) || !(await this.app.vault.adapter.exists(`${base}/manifest.json`))) return false;
      try {
        const m = JSON.parse(await this.app.vault.adapter.read(`${base}/manifest.json`));
        if (m.id !== p.id || cleanVersion(m.version) !== cleanVersion(p.version)) return false;
      } catch (_) { return false; }
    }
    return true;
  }

  async ensurePlugin(p, force) {
    const configDir = this.app.vault.configDir || ".obsidian";
    const base = `${configDir}/plugins/${p.id}`;
    await this.mkdirp(base);
    if (!force && await this.pluginMatches(base, p)) return false;

    const release = await this.findRelease(p);
    const assets = new Map((release.assets || []).map(a => [a.name, a.browser_download_url]));
    for (const name of ["manifest.json", "main.js"]) {
      const url = assets.get(name) || `https://github.com/${p.repo}/releases/download/${release.tag_name}/${name}`;
      const text = await this.getText(url);
      await this.app.vault.adapter.write(`${base}/${name}`, text);
    }
    const cssUrl = assets.get("styles.css");
    if (cssUrl) {
      try { await this.app.vault.adapter.write(`${base}/styles.css`, await this.getText(cssUrl)); } catch (_) {}
    } else {
      // Some plugins commit styles but do not attach it. It is optional in Obsidian.
      try {
        const raw = `https://raw.githubusercontent.com/${p.repo}/${release.tag_name}/styles.css`;
        await this.app.vault.adapter.write(`${base}/styles.css`, await this.getText(raw));
      } catch (_) {}
    }

    const manifest = JSON.parse(await this.app.vault.adapter.read(`${base}/manifest.json`));
    if (manifest.id !== p.id) throw new Error(`${p.id}: downloaded manifest id is ${manifest.id}`);
    if (cleanVersion(manifest.version) !== cleanVersion(p.version)) throw new Error(`${p.id}: expected ${p.version}, got ${manifest.version}`);
    return true;
  }

  async pluginMatches(base, p) {
    try {
      if (!(await this.app.vault.adapter.exists(`${base}/main.js`)) || !(await this.app.vault.adapter.exists(`${base}/manifest.json`))) return false;
      const m = JSON.parse(await this.app.vault.adapter.read(`${base}/manifest.json`));
      return m.id === p.id && cleanVersion(m.version) === cleanVersion(p.version);
    } catch (_) { return false; }
  }

  async findRelease(p) {
    const url = `https://api.github.com/repos/${p.repo}/releases?per_page=40`;
    const r = await requestUrl({ url, headers: { "Accept": "application/vnd.github+json" } });
    const releases = r.json || JSON.parse(r.text);
    const hit = releases.find(x => !x.draft && cleanVersion(x.tag_name) === cleanVersion(p.version));
    if (!hit) throw new Error(`${p.id}: release ${p.version} not found at ${p.repo}`);
    return hit;
  }

  async getText(url) {
    const r = await requestUrl({ url });
    if (typeof r.text !== "string" || !r.text.length) throw new Error(`Empty download: ${url}`);
    return r.text;
  }

  async mkdirp(path) {
    const adapter = this.app.vault.adapter;
    const parts = path.split("/").filter(Boolean);
    let cur = "";
    for (const part of parts) {
      cur = cur ? `${cur}/${part}` : part;
      if (!(await adapter.exists(cur))) {
        try { await adapter.mkdir(cur); } catch (_) {}
      }
    }
  }

  async writeStatus(lines, immediate) {
    const path = "99_System/01_Admin/Bootstrap Status.md";
    const body = [
      "# MDSE Bootstrap Status", "",
      `Last run: ${new Date().toISOString()}`, "",
      immediate ? "Plugin manager accepted immediate enable requests." : "A reload may be required to activate downloaded plugins.", "",
      "## Pinned stack", "", ...lines.map(x => `- ${x}`), "",
      "The bootstrap never overwrites plugin `data.json` files; the MDSE relationship and schema configuration remains vault-controlled.", ""
    ].join("\n");
    const f = this.app.vault.getAbstractFileByPath(path);
    if (f) await this.app.vault.modify(f, body); else await this.app.vault.create(path, body);
  }
};
