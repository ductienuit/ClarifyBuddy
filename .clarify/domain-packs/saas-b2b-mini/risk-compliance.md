# Risk & Compliance: B2B SaaS

- **Risk:** cross-tenant data leak → **Control:** enforce tenant scope on every
  query; never trust org id from the client.
- **Risk:** privilege escalation → **Control:** server-side role checks; block
  self-escalation and last-owner demotion.
- **Risk:** lost billing webhook → **Control:** idempotent webhook handling +
  reconciliation against the billing provider.
- **Compliance:** SOC 2 / GDPR — access changes and data exports must be audited;
  data residency may apply (OPEN QUESTION).
- **Audit:** log role changes, invites, deactivations, plan changes.
