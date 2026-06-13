# Common Flows: B2B SaaS

## Invite member
- **Actors:** Admin, Invitee.
- **Main path:** 1) Admin invites email + role 2) Invitation created/sent
  3) Invitee accepts 4) Membership created with role.
- **Branches:** invitee already a member; seat limit reached; invitation expires.

## Change role
- **Main path:** Admin selects member → picks new role → permissions recomputed.
- **Branches:** demoting the last owner (disallow); self-demotion.

## Subscription change
- **Main path:** Admin changes plan → entitlements updated → proration billed.
- **Branches:** downgrade below current usage (block or warn).
