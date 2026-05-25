# Example Run — Support Agent Studio

This artifact records a deterministic reviewer demo run for the MiMo approval pattern.

- Project: **Support Agent Studio**
- Domain: support automation
- Scenario: `support queue contains duplicate payment webhook failures after deploy`
- Status: `completed`
- Mode: `deterministic-reviewer-demo`
- Specialist agents: 5
- Estimated tokens: **41,453**
- Daily projection: **3,979,488 tokens/day**

## Findings

### Liquidity Scout
- Role: tracks pool depth, volatility spikes, and suspicious flow concentration
- Severity: `high`
- Confidence: `0.68`
- Estimated tokens: `8114`
- Finding: Liquidity Scout reviewed DeFi risk monitoring signal: support queue contains duplicate payment webhook failures after deploy. Risk pattern=high confidence=0.68.
- Recommendation: Run liquidity scout follow-up pass, capture artifacts, then prioritize high items first.

### Exploit Sentinel
- Role: maps events to known attack primitives and detects anomalous protocol behavior
- Severity: `medium`
- Confidence: `0.9`
- Estimated tokens: `10077`
- Finding: Exploit Sentinel reviewed DeFi risk monitoring signal: support queue contains duplicate payment webhook failures after deploy. Risk pattern=medium confidence=0.9.
- Recommendation: Run exploit sentinel follow-up pass, capture artifacts, then prioritize medium items first.

### Oracle Auditor
- Role: checks oracle drift, stale feeds, and manipulation windows
- Severity: `critical`
- Confidence: `0.91`
- Estimated tokens: `4987`
- Finding: Oracle Auditor reviewed DeFi risk monitoring signal: support queue contains duplicate payment webhook failures after deploy. Risk pattern=critical confidence=0.91.
- Recommendation: Run oracle auditor follow-up pass, capture artifacts, then prioritize critical items first.

### Treasury Guardian
- Role: scores treasury exposure and proposes emergency controls
- Severity: `high`
- Confidence: `0.81`
- Estimated tokens: `9522`
- Finding: Treasury Guardian reviewed DeFi risk monitoring signal: support queue contains duplicate payment webhook failures after deploy. Risk pattern=high confidence=0.81.
- Recommendation: Run treasury guardian follow-up pass, capture artifacts, then prioritize high items first.

### Incident Reporter
- Role: synthesizes operator-grade markdown incident reports
- Severity: `medium`
- Confidence: `0.88`
- Estimated tokens: `8753`
- Finding: Incident Reporter reviewed DeFi risk monitoring signal: support queue contains duplicate payment webhook failures after deploy. Risk pattern=medium confidence=0.88.
- Recommendation: Run incident reporter follow-up pass, capture artifacts, then prioritize medium items first.

