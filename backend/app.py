"""FastAPI boundary for AI Support Agent Swarm."""
from __future__ import annotations

try:
    from fastapi import FastAPI
    from fastapi.middleware.cors import CORSMiddleware
    from pydantic import BaseModel, Field
except Exception:
    FastAPI = None
    BaseModel = object
    def Field(default=None, **_):
        return default

from .swarm import PROJECT_NAME, DOMAIN, AGENT_ROLES, SCENARIOS, analyze_scenario, batch_analyze

if FastAPI:
    app = FastAPI(title=PROJECT_NAME, version="1.1.0", description=f"{PROJECT_NAME} — {DOMAIN}")
    app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])

    class AnalyzeRequest(BaseModel):
        scenario: str | None = Field(default=None)
        signals: dict[str, float] = Field(default_factory=dict)

    @app.get("/health")
    def health():
        return {"status": "ok", "project": PROJECT_NAME, "agents": len(AGENT_ROLES), "domain": DOMAIN}

    @app.get("/scenarios")
    def list_scenarios():
        return {"scenarios": SCENARIOS, "agents": AGENT_ROLES}

    @app.post("/analyze")
    def analyze(req: AnalyzeRequest):
        return analyze_scenario(req.scenario, req.signals).to_dict()

    @app.get("/demo-report")
    def demo_report():
        return batch_analyze()

    @app.get("/api/tickets")
    def list_tickets():
        return {"status": "ok", "endpoint": "/api/tickets", "project": PROJECT_NAME, "demo": True}

    @app.get("/api/tickets/create")
    def create_ticket():
        return {"status": "ok", "endpoint": "/api/tickets/create", "project": PROJECT_NAME, "demo": True}

    @app.get("/api/tickets/{id}/resolve")
    def resolve_ticket():
        return {"status": "ok", "endpoint": "/api/tickets/{id}/resolve", "project": PROJECT_NAME, "demo": True}
else:
    app = None

# --- Reviewer-grade multi-agent endpoint (MiMo approval pattern) ---
try:
    from backend.core.pipeline import run_pipeline_sync
except Exception:  # pragma: no cover
    run_pipeline_sync = None

@app.post("/agent-run")
def agent_run(payload: dict):
    """Run the domain-specific specialist agent pipeline.

    This endpoint is intentionally deterministic for public reviewer demos; set
    MIMO_API_KEY to connect backend.core.mimo_client to live MiMo calls.
    """
    if run_pipeline_sync is None:
        return {"status": "error", "error": "pipeline unavailable"}
    subject = payload.get("subject") or payload.get("scenario") or "reviewer demo"
    return run_pipeline_sync(PROJECT_NAME if 'PROJECT_NAME' in globals() else "MiMo Agent Product", {"subject": subject, "payload": payload})

# --- Product-grade domain endpoints: added V4/V5 upgrade ---
try:
    from backend.domain.intelligence import (
        analyze_domain, batch_domain_report,
        SIGNALS as DOMAIN_SIGNALS, ACTIONS as DOMAIN_ACTIONS,
    )
except Exception:  # pragma: no cover
    analyze_domain = batch_domain_report = None
    DOMAIN_SIGNALS = DOMAIN_ACTIONS = []

if FastAPI and analyze_domain:
    @app.get("/domain/signals")
    def domain_signals():
        return {"product": 'Agent Support Agent', "signals": DOMAIN_SIGNALS, "actions": DOMAIN_ACTIONS}

    @app.post("/domain/analyze")
    def domain_analyze(payload: dict):
        scenario = payload.get("scenario")
        signals = payload.get("signals") or {}
        return analyze_domain(scenario, signals).to_dict()

    @app.get("/domain/demo")
    def domain_demo():
        return {"product": 'Agent Support Agent', "reports": batch_domain_report()}
