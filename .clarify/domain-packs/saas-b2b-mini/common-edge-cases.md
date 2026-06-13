# Common Edge Cases: B2B SaaS

- **Boundary:** org with 1 member; seat limit exactly reached; max roles.
- **Negative/invalid:** invite an existing member; invalid email; assign a
  non-existent role.
- **Exception/failure:** SSO provider down; billing webhook lost.
- **State:** demote the last Owner; accept an expired invitation; act after
  deactivation.
- **Concurrency:** two admins change the same member's role; simultaneous invites
  consuming the last seat.
- **Permission:** member performs an admin-only action; cross-tenant data access.
