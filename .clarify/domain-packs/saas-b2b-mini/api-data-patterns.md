# API & Data Patterns: B2B SaaS

## Entities & source of truth
- Org/Membership/Role — owned by the identity/access service (authoritative).
- Subscription/Plan — owned by the billing service; entitlements derived from it.

## Common endpoints
- POST /orgs/{id}/invitations — invite a member (role in body).
- PATCH /orgs/{id}/members/{uid} — change role.
- POST /orgs/{id}/subscription — change plan.

## Integration patterns
- Every query is **tenant-scoped**; org id derived from the auth context, never
  trusted from the client body.
- Billing changes via webhook: verify signature, dedupe by event id (idempotent).
- Emit member.invited / role.changed events for notifications + audit.
