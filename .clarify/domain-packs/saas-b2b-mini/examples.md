# Examples: B2B SaaS

## Role change
- **Weak:** "Admins can change user roles."
- **Strong:** "An Org Admin can change another member's role; the system rejects
  the change if it would remove the last Owner or if the actor is changing their
  own role to a higher privilege. The change is audit-logged and takes effect on
  the member's next request. ASSUMPTION: changes apply immediately, not at next
  login."
- **Anti-patterns fixed:** missing-permission, undefined-state (last-owner),
  missing-audit-log, hidden-assumption.

## Invite
- **Weak:** "Invite users to the org."
- **Strong:** "An Admin invites an email with a role; if seats are full the
  invite is blocked with an upgrade prompt; invitations expire after 7 days
  (confirm). Accepting creates an active membership."
- **Anti-patterns fixed:** missing-edge-case (seat limit), undefined-state
  (expiry), ambiguous-actor.
