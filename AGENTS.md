# AI / Agent Rules

If `99_System/10_Docs/00 - Current State.md` exists, read it first; it governs the methodology workspace. A lean generated engineering vault intentionally omits that registry.

For a normal engineering vault, read these before creating, moving, or editing model content:

1. `99_System/02_AI/AI_INSTRUCTIONS.md`
2. `99_System/10_Docs/MDSE Modeling Ruleset 1.23.md`
3. `99_System/10_Docs/MDSE Vault File and Folder Structure 0.8.md`
4. the runtime schemas under `99_System/03_Schemas/`

The essentials:

- Preserve the controlled root, `.obsidian/`, and `99_System/` runtime structure. Do not invent replacement system files when something is missing.
- Folder placement is navigation, not semantic meaning. Use the filesystem contract before creating or reorganizing folders.
- Create notes from the class template in `99_System/05_Templates`, and fill in `uid` and `id` yourself by the rules in `AI_INSTRUCTIONS.md`. You cannot run Templater, but the result must be identical.
- Use your author code only for notes you create with no direct user instruction. When a user directs the note, use the user's code.
- Leave `status` at the template default. A person reviews.
- Never delete a note; retire it. Never reuse an `id`. Never change an existing `uid` or `id`.
- Never invent missing source facts. Reuse concepts instead of duplicating them.
