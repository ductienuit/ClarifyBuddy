# Example: SaaS Role Management

Demonstrates `/clarify:from-idea` → `/clarify:audit` using the
`saas-b2b-mini` domain pack.

## Run

```
/clarify:from-idea "Let org admins manage member roles and invite teammates"
```

(Select `saas-b2b-mini` when prompted.)

## What Clarify surfaces
- Last-Owner protection (undefined-state) and self-escalation (missing-permission).
- Seat-limit edge case on invite (missing-edge-case).
- Tenant isolation as a risk/control (cross-tenant access).
- Audit logging of role changes (missing-audit-log).

See `input-idea.md` for the seed idea.
