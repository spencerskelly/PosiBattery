# Verification Model

The current verification model separates reusable verification intent from execution evidence.

- **Step** — reusable setup/configuration/action step.
- **Verification** — test, analysis, inspection, or demonstration that verifies Requirements.
- **Procedure** — ordered `sequence` of Steps and/or Verifications.
- **Setup** — available source/load/meter/interface/environment/fixture capability.
- **Plan** — selected sequence for a campaign/run plus `usesSetup`, `plannedDUTs`, and `scopeRequirements`.
- **Result** — one execution record linked by `resultOf`; it carries `outcome`, DUT, equipment used, and evidence.

Equipment fit is deliberate: Steps/Verifications declare `requires*`; Setups declare `provides*`. This supports filtering without turning every bench device into a hard-coded property.
