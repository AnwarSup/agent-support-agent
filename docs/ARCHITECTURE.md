# Crypto Support Agent Architecture

## Purpose

AI support desk for wallet issues, transaction debugging, escalation routing, and knowledge-base improvement.

## Runtime loop

1. **Observe** — collect domain signals: ticket_severity, tx_confirmation_age, refund_risk, user_sentiment, kb_gap_score.
2. **Orient** — map the active scenario to specialist agent responsibilities.
3. **Decide** — score severity, confidence, and operator urgency.
4. **Act** — emit next actions that a human operator can verify.
5. **Reflect** — attach trace IDs and deterministic evidence for review.

## Components

- `backend/swarm.py` — pure Python reasoning core, safe for CI and static demos.
- `backend/app.py` — FastAPI wrapper for product integration.
- `cli.py` — terminal demo path for reviewers.
- `index.html` — front-facing dashboard surface.

## Agent responsibilities

- `Ticket Classifier`: owns one part of the analysis loop.
- `Transaction Debugger`: owns one part of the analysis loop.
- `Policy-Aware Responder`: owns one part of the analysis loop.
- `Escalation Router`: owns one part of the analysis loop.
- `Knowledge Gap Miner`: owns one part of the analysis loop.

## Production extension points

- Replace deterministic signals with live connectors.
- Persist reports in Postgres or SQLite.
- Add auth and organization workspaces.
- Add export hooks for Slack, Discord, Telegram, or email.
