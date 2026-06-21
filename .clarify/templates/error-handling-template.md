<!-- Working structure for the `error-handling` engine (folded into the URD §3.7 — no separate file). -->

# Error Handling & Message Mapping

Maps each failure in the flow to a code, the entity state and transaction status
it leaves behind, the internal message, the **user-facing message**, and the
follow-up action. This is what FE, BE, QA, support, and legal align on. Do not
invent messages silently; mark unknowns `OPEN QUESTION`.

> Altitude: business reviewers read **Scenario / User message / Required action /
> Needs-ops**. Dev/QA also use **Code / HTTP / Entity state / Transaction status /
> Retryable / Log level / Owner**.

<!-- Working structure for building the in-document "Error code & message table"
     (Principle 13.8). Not emitted as a separate file. -->

## Error map
Each row maps back to the flow/step it occurs in (Flow `F0n-Name` / step # from the
flow analysis), so the error is anchored in the process.
| Code | Flow / Step | Scenario | HTTP / API status | Entity state after error | Transaction / operation status after error | Internal message | User-facing message | Retryable? | Required action | Needs Ops/CS? | Owner |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| <CODE_001> | <F01 / step 3> | <e.g. amount below minimum> | 422 | <unchanged / none created> | Failed | <internal> | <plain user message, no jargon> | yes/no | <next step> | no | <service> |

## Coverage checklist (cover each group that applies)
- [ ] **Eligibility / input** — not authenticated/KYC, below min, above limit, invalid source.
- [ ] **Balance / account** — insufficient funds, account blocked/frozen, debit not allowed.
- [ ] **Product / config** — option/tenor unavailable, rate/version changed before confirm.
- [ ] **Authentication** — wrong code, expired, retry-limit exceeded, user cancelled.
- [ ] **Money/processing** — debit failed; debit OK but creation failed; timeout; duplicate request.
- [ ] **System** — service unavailable / maintenance, unexpected error.

## Rules
- User messages must be plain language — **no** `ledger`, `idempotency`, `GL`,
  `accrual`, `debit`, `schema`, `API`, `timeout code`, or internal service-name
  jargon.
- For "money moved but record not created", the user message must NOT assert a
  wrong final state — say it is being processed and how to check/contact.
- Every row states the entity state and transaction/operation status it leaves,
  so the client, support, and operations can resolve it consistently.

## Gaps
- <flows with failures but no mapped code/message (`missing-error-message-mapping`)>
