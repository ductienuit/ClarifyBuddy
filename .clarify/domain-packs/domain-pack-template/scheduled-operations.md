# Scheduled Operations: <Domain>

Batch / scheduled jobs this domain typically needs. For each job give the
schedule/trigger, idempotency & resume strategy, inputs, outputs, and the
downstream consumers of those outputs.

| Job | Schedule / Trigger | Idempotency / Resume | Inputs | Outputs | Downstream consumers |
| --- | --- | --- | --- | --- | --- |
| <…> | <e.g. daily 02:00 UTC> | <key / resume strategy> | <…> | <…> | <…> |

## Job state model
- **States:** scheduled → running → completed / failed → retried.
- **Illegal / risky:** overlapping runs, double-posting on rerun, partial-batch
  completion with no resume point.
