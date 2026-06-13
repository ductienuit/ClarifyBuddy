# Domain: B2B SaaS (mini)

Multi-tenant software sold to organizations, with users grouped into accounts,
role-based access, subscriptions, and admin controls.

## Primary actors / roles
- Org Owner / Admin — manages members, roles, billing.
- Member — uses the product within their org's permissions.
- Billing contact — manages the subscription.
- System — enforces tenancy isolation and entitlements.

## Core entities
- Organization (tenant), User, Membership, Role, Permission, Subscription, Plan,
  Invitation.

## Typical goals
- Role/permission management, team invites, SSO, billing/plans, usage limits.

## When to select this pack
- The PRD mentions organizations/tenants, roles, permissions, members, seats,
  plans, or subscriptions.
