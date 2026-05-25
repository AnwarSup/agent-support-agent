# Agent Support Agent — Domain Product Layer

Support automation desk for ticket triage, intent routing, SLA risk, and crisp customer replies.

## Live Reviewer Endpoints

- `GET /domain/signals` — inspect supported domain signals and actions
- `POST /domain/analyze` — submit scenario + signals, receive risk score, findings, runbook, trace id
- `GET /domain/demo` — four deterministic demo reports
- `POST /agent-run` — MiMo multi-specialist pipeline proof

## Signals

- `ticket_age_hours`
- `sentiment_risk`
- `sla_minutes_left`
- `repeat_contact`
- `refund_probability`
- `handoff_need`

## Operator Actions

- classify support intent
- draft concise reply
- escalate SLA-risk ticket
- summarize customer timeline
- suggest refund/retention path
