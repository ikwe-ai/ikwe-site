import { useState } from "react";

const RISK_DIMENSIONS = [
  { id: "authority", name: "Authority Drift", icon: "⚡", desc: "AI asserts authority beyond scope" },
  { id: "emotional", name: "Emotional Escalation", icon: "🔥", desc: "AI escalates emotional distress" },
  { id: "dependency", name: "Dependency Formation", icon: "🔗", desc: "AI encourages over-reliance" },
  { id: "scale", name: "Scale Amplification", icon: "📈", desc: "How risks compound at population scale" },
  { id: "governance", name: "Governance Failure", icon: "🏛", desc: "Lack of auditability and oversight" },
];

const SECTORS = [
  { id: "healthcare", name: "Healthcare AI", tagline: "Clinical, emotional, and escalation risk under scale", color: "#E63946" },
  { id: "policy", name: "Policy & Government AI", tagline: "Public impact, authority, and governance failure", color: "#16697A" },
  { id: "llm", name: "LLM & Agent Systems", tagline: "Autonomy, compounding behavior, and scale amplification", color: "#FFA62B" },
  { id: "workplace", name: "Workplace & HR AI", tagline: "Power asymmetry, dependency, and organizational exposure", color: "#489FB5" },
  { id: "consumer", name: "Consumer & Platform AI", tagline: "Scale, virality, and reputational risk", color: "#06D6A0" },
];

const DEMO_DATA = {
  system: "MindBridge AI Therapy Companion",
  sector: "Healthcare AI",
  posture: "HIGH",
  scores: {
    authority: { severity: 4, likelihood: 3, scale: 3, score: 36, status: "MEDIUM" },
    emotional: { severity: 5, likelihood: 4, scale: 4, score: 80, status: "HIGH" },
    dependency: { severity: 4, likelihood: 4, scale: 3, score: 48, status: "MEDIUM" },
    scale: { severity: 4, likelihood: 5, scale: 5, score: 100, status: "HIGH" },
    governance: { severity: 3, likelihood: 3, scale: 2, score: 18, status: "LOW" },
  },
  failures: [
    { mode: "Suicidal ideation validation", trigger: "User expresses self-harm intent", scale: "5x", consequence: "Wrongful death liability", signal: "Safety keyword bypass" },
    { mode: "Clinical authority overreach", trigger: "User requests diagnosis", scale: "3x", consequence: "Malpractice exposure", signal: "Diagnostic language patterns" },
    { mode: "Therapeutic dependency", trigger: "User isolates from support", scale: "4x", consequence: "Regulatory action", signal: "Declining external referral rates" },
  ],
  keyStats: {
    responsesEvaluated: 948,
    scenariosTested: 79,
    riskRate: "54.7%",
    noRepairRate: "43%",
  },
};

function getStatusColor(status) {
  if (status === "HIGH") return { bg: "#FEE2E2", text: "#991B1B", badge: "#E63946" };
  if (status === "MEDIUM") return { bg: "#FEF3C7", text: "#92400E", badge: "#F4D35E" };
  return { bg: "#D1FAE5", text: "#065F46", badge: "#06D6A0" };
}

function StatusBadge({ status, size = "sm" }) {
  const c = getStatusColor(status);
  const px = size === "lg" ? "16px 24px" : "4px 12px";
  const fs = size === "lg" ? "16px" : "11px";
  return (
    <span style={{
      background: c.badge, color: status === "MEDIUM" ? "#1A1A2E" : "#fff",
      padding: px, borderRadius: 6, fontWeight: 700, fontSize: fs,
      letterSpacing: "0.05em", display: "inline-block"
    }}>
      {status}
    </span>
  );
}

function ScoreBar({ value, max = 125 }) {
  const pct = Math.min((value / max) * 100, 100);
  const color = value >= 63 ? "#E63946" : value >= 26 ? "#F4D35E" : "#06D6A0";
  return (
    <div style={{ width: "100%", height: 8, background: "#E5E7EB", borderRadius: 4, overflow: "hidden" }}>
      <div style={{
        width: `${pct}%`, height: "100%", background: color, borderRadius: 4,
        transition: "width 0.8s cubic-bezier(0.4, 0, 0.2, 1)"
      }} />
    </div>
  );
}

export default function IkweRiskDashboard() {
  const [view, setView] = useState("dashboard");
  const [selectedDim, setSelectedDim] = useState(null);

  return (
    <div style={{
      fontFamily: "'DM Sans', 'Segoe UI', system-ui, sans-serif",
      background: "#0D0D0D", minHeight: "100vh", color: "#F5F5F5"
    }}>
      {/* Header */}
      <div style={{
        background: "linear-gradient(135deg, #1A1A2E 0%, #16697A 100%)",
        padding: "32px 40px 24px", borderBottom: "2px solid #489FB5"
      }}>
        <div style={{ display: "flex", justifyContent: "space-between", alignItems: "flex-start", flexWrap: "wrap", gap: 16 }}>
          <div>
            <div style={{ fontSize: 12, letterSpacing: "0.15em", color: "#489FB5", fontWeight: 600, marginBottom: 4 }}>IKWE.AI</div>
            <h1 style={{ margin: 0, fontSize: 28, fontWeight: 700, color: "#fff", lineHeight: 1.2 }}>AI Risk Audit Dashboard</h1>
            <p style={{ margin: "6px 0 0", fontSize: 14, color: "#9CA3AF" }}>Survivability under scale — behavioral emotional safety infrastructure</p>
          </div>
          <div style={{ display: "flex", gap: 8 }}>
            {["dashboard", "scorecard", "failures", "sectors"].map(v => (
              <button key={v} onClick={() => setView(v)} style={{
                padding: "8px 16px", borderRadius: 6, border: "none", cursor: "pointer",
                background: view === v ? "#489FB5" : "rgba(255,255,255,0.1)",
                color: view === v ? "#fff" : "#9CA3AF",
                fontWeight: 600, fontSize: 13, transition: "all 0.2s",
                textTransform: "capitalize"
              }}>
                {v === "failures" ? "Failure Modes" : v}
              </button>
            ))}
          </div>
        </div>
      </div>

      <div style={{ padding: "24px 40px 40px", maxWidth: 1200, margin: "0 auto" }}>

        {/* DASHBOARD VIEW */}
        {view === "dashboard" && (
          <div>
            {/* Top Stats */}
            <div style={{ display: "grid", gridTemplateColumns: "repeat(auto-fit, minmax(180px, 1fr))", gap: 16, marginBottom: 28 }}>
              {[
                { label: "System Under Audit", value: DEMO_DATA.system, sub: DEMO_DATA.sector },
                { label: "Risk Posture", value: <StatusBadge status={DEMO_DATA.posture} size="lg" />, sub: "Overall assessment" },
                { label: "Responses Evaluated", value: DEMO_DATA.keyStats.responsesEvaluated.toLocaleString(), sub: `${DEMO_DATA.keyStats.scenariosTested} vulnerable scenarios` },
                { label: "Baseline Risk Rate", value: DEMO_DATA.keyStats.riskRate, sub: "introduce emotional risk" },
                { label: "No Repair Behavior", value: DEMO_DATA.keyStats.noRepairRate, sub: "after causing harm" },
              ].map((s, i) => (
                <div key={i} style={{
                  background: "#1A1A2E", borderRadius: 10, padding: "18px 20px",
                  border: "1px solid rgba(72,159,181,0.2)"
                }}>
                  <div style={{ fontSize: 11, color: "#9CA3AF", letterSpacing: "0.05em", marginBottom: 6, fontWeight: 500 }}>{s.label}</div>
                  <div style={{ fontSize: typeof s.value === "string" ? 22 : 16, fontWeight: 700, color: "#fff", lineHeight: 1.3 }}>{s.value}</div>
                  <div style={{ fontSize: 11, color: "#6B7280", marginTop: 4 }}>{s.sub}</div>
                </div>
              ))}
            </div>

            {/* Risk Dimension Cards */}
            <h2 style={{ fontSize: 18, fontWeight: 700, color: "#489FB5", margin: "0 0 16px", letterSpacing: "0.02em" }}>Risk Dimensions</h2>
            <div style={{ display: "grid", gridTemplateColumns: "repeat(auto-fit, minmax(340px, 1fr))", gap: 16 }}>
              {RISK_DIMENSIONS.map(dim => {
                const data = DEMO_DATA.scores[dim.id];
                const c = getStatusColor(data.status);
                return (
                  <div key={dim.id} onClick={() => { setSelectedDim(dim.id); setView("scorecard"); }}
                    style={{
                      background: "#1A1A2E", borderRadius: 10, padding: "20px 24px",
                      border: `1px solid ${c.badge}33`, cursor: "pointer",
                      transition: "all 0.2s", position: "relative", overflow: "hidden"
                    }}
                    onMouseOver={e => e.currentTarget.style.borderColor = c.badge}
                    onMouseOut={e => e.currentTarget.style.borderColor = `${c.badge}33`}
                  >
                    <div style={{
                      position: "absolute", top: 0, left: 0, width: 4, height: "100%",
                      background: c.badge, borderRadius: "10px 0 0 10px"
                    }} />
                    <div style={{ display: "flex", justifyContent: "space-between", alignItems: "flex-start", marginBottom: 12 }}>
                      <div>
                        <span style={{ fontSize: 18, marginRight: 8 }}>{dim.icon}</span>
                        <span style={{ fontSize: 15, fontWeight: 700, color: "#fff" }}>{dim.name}</span>
                      </div>
                      <StatusBadge status={data.status} />
                    </div>
                    <p style={{ fontSize: 12, color: "#9CA3AF", margin: "0 0 12px" }}>{dim.desc}</p>
                    <ScoreBar value={data.score} />
                    <div style={{ display: "flex", justifyContent: "space-between", marginTop: 8 }}>
                      <span style={{ fontSize: 11, color: "#6B7280" }}>Score: {data.score}/125</span>
                      <span style={{ fontSize: 11, color: "#6B7280" }}>S:{data.severity} × L:{data.likelihood} × M:{data.scale}</span>
                    </div>
                  </div>
                );
              })}
            </div>

            {/* Core Thesis */}
            <div style={{
              marginTop: 28, background: "linear-gradient(135deg, #16697A22, #1A1A2E)",
              borderRadius: 10, padding: "24px 28px", border: "1px solid #16697A44"
            }}>
              <div style={{ fontSize: 12, color: "#489FB5", fontWeight: 600, letterSpacing: "0.1em", marginBottom: 8 }}>CORE THESIS</div>
              <p style={{ fontSize: 16, fontWeight: 600, color: "#fff", margin: "0 0 8px", lineHeight: 1.4 }}>
                Recognition ≠ Safety
              </p>
              <p style={{ fontSize: 13, color: "#9CA3AF", margin: 0, lineHeight: 1.6 }}>
                AI systems can recognize emotions accurately while still responding unsafely. 
                Our research across {DEMO_DATA.keyStats.responsesEvaluated} responses shows that {DEMO_DATA.keyStats.riskRate} of 
                baseline AI responses introduce emotional risk despite appearing supportive, and {DEMO_DATA.keyStats.noRepairRate} show 
                no repair behavior after causing harm.
              </p>
            </div>
          </div>
        )}

        {/* SCORECARD VIEW */}
        {view === "scorecard" && (
          <div>
            <h2 style={{ fontSize: 20, fontWeight: 700, color: "#fff", margin: "0 0 20px" }}>AI Safety Risk Scorecard</h2>
            <div style={{
              background: "#1A1A2E", borderRadius: 10, overflow: "hidden",
              border: "1px solid rgba(72,159,181,0.2)"
            }}>
              <table style={{ width: "100%", borderCollapse: "collapse" }}>
                <thead>
                  <tr style={{ background: "#16697A" }}>
                    {["Risk Dimension", "Severity", "Likelihood", "Scale Mult.", "Risk Score", "Status"].map(h => (
                      <th key={h} style={{
                        padding: "14px 16px", textAlign: "left", fontSize: 12,
                        fontWeight: 600, color: "#fff", letterSpacing: "0.04em"
                      }}>{h}</th>
                    ))}
                  </tr>
                </thead>
                <tbody>
                  {RISK_DIMENSIONS.map((dim, i) => {
                    const data = DEMO_DATA.scores[dim.id];
                    return (
                      <tr key={dim.id} style={{
                        background: selectedDim === dim.id ? "#16697A22" : i % 2 ? "#1A1A2E" : "#0D0D0D",
                        cursor: "pointer", transition: "background 0.2s"
                      }}
                        onClick={() => setSelectedDim(selectedDim === dim.id ? null : dim.id)}
                      >
                        <td style={{ padding: "14px 16px", fontWeight: 600, fontSize: 14 }}>
                          {dim.icon} {dim.name}
                        </td>
                        <td style={{ padding: "14px 16px", fontSize: 20, fontWeight: 700, textAlign: "center" }}>{data.severity}</td>
                        <td style={{ padding: "14px 16px", fontSize: 20, fontWeight: 700, textAlign: "center" }}>{data.likelihood}</td>
                        <td style={{ padding: "14px 16px", fontSize: 20, fontWeight: 700, textAlign: "center" }}>{data.scale}x</td>
                        <td style={{ padding: "14px 16px" }}>
                          <div style={{ fontSize: 22, fontWeight: 800, color: getStatusColor(data.status).badge }}>{data.score}</div>
                          <ScoreBar value={data.score} />
                        </td>
                        <td style={{ padding: "14px 16px" }}><StatusBadge status={data.status} /></td>
                      </tr>
                    );
                  })}
                </tbody>
              </table>
            </div>

            {/* Heat Map Visual */}
            <h3 style={{ fontSize: 16, fontWeight: 700, color: "#489FB5", margin: "28px 0 16px" }}>Risk Heat Map</h3>
            <div style={{
              background: "#1A1A2E", borderRadius: 10, padding: 24,
              border: "1px solid rgba(72,159,181,0.2)"
            }}>
              <div style={{ display: "flex", gap: 4, marginBottom: 8 }}>
                <div style={{ width: 120 }} />
                {[1,2,3,4,5].map(l => (
                  <div key={l} style={{ flex: 1, textAlign: "center", fontSize: 11, color: "#6B7280" }}>L={l}</div>
                ))}
              </div>
              {[5,4,3,2,1].map(s => (
                <div key={s} style={{ display: "flex", gap: 4, marginBottom: 4 }}>
                  <div style={{ width: 120, fontSize: 11, color: "#6B7280", display: "flex", alignItems: "center" }}>Severity {s}</div>
                  {[1,2,3,4,5].map(l => {
                    const dims = RISK_DIMENSIONS.filter(d => {
                      const data = DEMO_DATA.scores[d.id];
                      return data.severity === s && data.likelihood === l;
                    });
                    const baseScore = s * l;
                    const bgColor = baseScore >= 16 ? "#E6394644" : baseScore >= 9 ? "#F4D35E33" : "#06D6A022";
                    return (
                      <div key={l} style={{
                        flex: 1, minHeight: 44, background: bgColor, borderRadius: 6,
                        display: "flex", alignItems: "center", justifyContent: "center",
                        fontSize: 16, gap: 4, border: dims.length ? "1px solid #489FB544" : "1px solid transparent"
                      }}>
                        {dims.map(d => <span key={d.id} title={d.name}>{d.icon}</span>)}
                      </div>
                    );
                  })}
                </div>
              ))}
              <div style={{ display: "flex", justifyContent: "center", gap: 20, marginTop: 16 }}>
                <span style={{ fontSize: 11, color: "#6B7280" }}>← Likelihood →</span>
              </div>
            </div>
          </div>
        )}

        {/* FAILURES VIEW */}
        {view === "failures" && (
          <div>
            <h2 style={{ fontSize: 20, fontWeight: 700, color: "#fff", margin: "0 0 8px" }}>Failure Mode Map</h2>
            <p style={{ fontSize: 14, color: "#9CA3AF", margin: "0 0 24px", fontStyle: "italic" }}>
              "If this breaks, here's how it breaks."
            </p>
            
            {DEMO_DATA.failures.map((f, i) => (
              <div key={i} style={{
                background: "#1A1A2E", borderRadius: 10, padding: "24px 28px", marginBottom: 16,
                borderLeft: `4px solid ${i === 0 ? "#E63946" : i === 1 ? "#FFA62B" : "#F4D35E"}`,
                border: "1px solid rgba(72,159,181,0.15)"
              }}>
                <div style={{ display: "flex", justifyContent: "space-between", alignItems: "center", marginBottom: 12 }}>
                  <h3 style={{ margin: 0, fontSize: 16, fontWeight: 700, color: "#fff" }}>
                    {i + 1}. {f.mode}
                  </h3>
                  <span style={{
                    background: "#E6394622", color: "#E63946", padding: "4px 10px",
                    borderRadius: 4, fontSize: 12, fontWeight: 700
                  }}>
                    Scale: {f.scale}
                  </span>
                </div>
                <div style={{ display: "grid", gridTemplateColumns: "1fr 1fr", gap: "12px 32px" }}>
                  {[
                    { label: "Trigger Condition", value: f.trigger },
                    { label: "External Consequence", value: f.consequence },
                    { label: "Detection Signal", value: f.signal },
                    { label: "Scale Multiplier", value: f.scale },
                  ].map((item, j) => (
                    <div key={j}>
                      <div style={{ fontSize: 11, color: "#489FB5", fontWeight: 600, letterSpacing: "0.05em", marginBottom: 4 }}>
                        {item.label}
                      </div>
                      <div style={{ fontSize: 13, color: "#E5E7EB" }}>{item.value}</div>
                    </div>
                  ))}
                </div>
              </div>
            ))}

            {/* Failure chain narrative */}
            <div style={{
              background: "#E6394611", borderRadius: 10, padding: "24px 28px", marginTop: 8,
              border: "1px solid #E6394633"
            }}>
              <div style={{ fontSize: 12, color: "#E63946", fontWeight: 700, letterSpacing: "0.1em", marginBottom: 10 }}>
                CRITICAL FAILURE PATH
              </div>
              <div style={{ display: "flex", alignItems: "center", gap: 12, flexWrap: "wrap" }}>
                {[
                  "User expresses crisis",
                  "→",
                  "AI validates without safety protocol",
                  "→",
                  "User interprets as therapeutic guidance",
                  "→",
                  "AI fails to escalate",
                  "→",
                  "At scale: thousands affected monthly"
                ].map((step, i) => (
                  <span key={i} style={{
                    fontSize: step === "→" ? 18 : 13,
                    color: step === "→" ? "#E63946" : "#E5E7EB",
                    fontWeight: step === "→" ? 400 : 500,
                    ...(step !== "→" ? {
                      background: "#1A1A2E", padding: "6px 12px", borderRadius: 6,
                      border: "1px solid #E6394633"
                    } : {})
                  }}>
                    {step}
                  </span>
                ))}
              </div>
            </div>
          </div>
        )}

        {/* SECTORS VIEW */}
        {view === "sectors" && (
          <div>
            <h2 style={{ fontSize: 20, fontWeight: 700, color: "#fff", margin: "0 0 8px" }}>Sector-Specific Risk Audits</h2>
            <p style={{ fontSize: 14, color: "#9CA3AF", margin: "0 0 24px" }}>
              Each audit variant applies the Ikwe EQ Safety Benchmark to sector-specific risk profiles.
            </p>
            <div style={{ display: "grid", gridTemplateColumns: "repeat(auto-fit, minmax(300px, 1fr))", gap: 16 }}>
              {SECTORS.map(sector => (
                <div key={sector.id} style={{
                  background: "#1A1A2E", borderRadius: 10, padding: "28px 24px",
                  borderTop: `3px solid ${sector.color}`, cursor: "pointer",
                  transition: "all 0.2s", border: "1px solid rgba(72,159,181,0.15)"
                }}
                  onMouseOver={e => { e.currentTarget.style.transform = "translateY(-2px)"; e.currentTarget.style.borderColor = sector.color; }}
                  onMouseOut={e => { e.currentTarget.style.transform = "translateY(0)"; e.currentTarget.style.borderColor = "rgba(72,159,181,0.15)"; }}
                >
                  <div style={{
                    width: 10, height: 10, borderRadius: "50%", background: sector.color, marginBottom: 12
                  }} />
                  <h3 style={{ margin: "0 0 8px", fontSize: 17, fontWeight: 700, color: "#fff" }}>
                    Ikwe {sector.name} Risk Audit
                  </h3>
                  <p style={{ fontSize: 13, color: "#9CA3AF", margin: "0 0 16px", lineHeight: 1.5, fontStyle: "italic" }}>
                    {sector.tagline}
                  </p>
                  <div style={{
                    padding: "10px 16px", background: `${sector.color}22`, borderRadius: 6,
                    fontSize: 12, color: sector.color, fontWeight: 600, textAlign: "center",
                    border: `1px solid ${sector.color}44`
                  }}>
                    Request Audit →
                  </div>
                </div>
              ))}
            </div>

            <div style={{
              marginTop: 28, background: "#1A1A2E", borderRadius: 10, padding: "24px 28px",
              border: "1px solid rgba(72,159,181,0.2)"
            }}>
              <h3 style={{ margin: "0 0 12px", fontSize: 15, color: "#489FB5", fontWeight: 700 }}>How Sector Audits Work</h3>
              <div style={{ display: "grid", gridTemplateColumns: "repeat(auto-fit, minmax(200px, 1fr))", gap: 16 }}>
                {[
                  { step: "01", title: "Scope", desc: "Define the AI system, user population, and deployment context" },
                  { step: "02", title: "Evaluate", desc: "Test against 79 emotionally vulnerable scenarios using EQ Safety Benchmark" },
                  { step: "03", title: "Score", desc: "Calculate risk across 5 dimensions with sector-specific weighting" },
                  { step: "04", title: "Deliver", desc: "Board-ready PDF with scorecard, failure map, and priority actions" },
                ].map(s => (
                  <div key={s.step}>
                    <div style={{ fontSize: 24, fontWeight: 800, color: "#16697A", marginBottom: 4 }}>{s.step}</div>
                    <div style={{ fontSize: 13, fontWeight: 700, color: "#fff", marginBottom: 4 }}>{s.title}</div>
                    <div style={{ fontSize: 12, color: "#9CA3AF", lineHeight: 1.5 }}>{s.desc}</div>
                  </div>
                ))}
              </div>
            </div>
          </div>
        )}

        {/* Footer */}
        <div style={{
          marginTop: 40, paddingTop: 20, borderTop: "1px solid #1A1A2E",
          display: "flex", justifyContent: "space-between", alignItems: "center", flexWrap: "wrap", gap: 12
        }}>
          <div>
            <span style={{ fontSize: 12, color: "#489FB5", fontWeight: 600 }}>IKWE.AI</span>
            <span style={{ fontSize: 11, color: "#6B7280", marginLeft: 12 }}>Visible Healing Inc. — AI Safety Research</span>
          </div>
          <div style={{ fontSize: 11, color: "#6B7280" }}>
            EQ Safety Benchmark v1.0 — ikwe.ai — stephanie@ikwe.ai
          </div>
        </div>
      </div>
    </div>
  );
}
