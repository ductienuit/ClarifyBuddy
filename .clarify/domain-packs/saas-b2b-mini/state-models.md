# State Models: B2B SaaS

## Membership
- **States:** invited → active → deactivated; plus declined, expired.
- **Transitions:** invited → active (accept); invited → expired (timeout);
  active → deactivated (admin removes).
- **Illegal:** deactivated → invited; demoting the last Owner.

## Subscription
- **States:** trialing → active → past_due → cancelled.
- **Transitions:** active → past_due (payment fails); past_due → active (paid);
  any → cancelled.
- **Terminal:** cancelled.
