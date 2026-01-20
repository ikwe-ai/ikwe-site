# Ikwe.ai Research Portal

**URL:** `research.ikwe.ai`  
**Purpose:** Secure, login-protected research execution environment

---

## Architecture

```
research.ikwe.ai
├── / (landing + login gate)
├── /study-ii (execution tool)
│
└── /.netlify/functions/
    ├── health.js
    ├── scenarios.js
    ├── runs.js
    ├── fetch.js
    ├── export.js
    └── stats.js
```

**Data Flow:**
1. User logs in via Netlify Identity
2. Frontend calls Netlify Functions (authenticated)
3. Functions write to GitHub (append-only)
4. Functions sync metadata to Notion (mirror only)

---

## Security Model

- **Authentication:** Netlify Identity (invite-only)
- **Authorization:** JWT verified on every API call
- **Data Storage:** GitHub (canonical, versioned)
- **Audit Trail:** Every write creates a Git commit

---

## Environment Variables (Netlify Dashboard)

```
# Required
ANTHROPIC_API_KEY=sk-ant-...
GITHUB_TOKEN=ghp_...
GITHUB_REPO=ikwe-ai/ikwe-research

# Optional
OPENAI_API_KEY=sk-proj-...
GOOGLE_API_KEY=AI...
NOTION_API_KEY=secret_...
NOTION_SCENARIOS_DB=...
NOTION_RUNS_DB=...
```

---

## Deployment

### 1. Create Netlify Site

```bash
# In this directory
netlify init
netlify deploy --prod
```

### 2. Configure Custom Domain

In Netlify dashboard:
- Domain settings → Add custom domain → `research.ikwe.ai`

In your DNS (Cloudflare/Namecheap):
- Add CNAME: `research` → `<site>.netlify.app`

### 3. Enable Netlify Identity

In Netlify dashboard:
- Site settings → Identity → Enable
- Registration: Invite only
- Invite yourself

### 4. Set Environment Variables

In Netlify dashboard:
- Site settings → Environment variables
- Add all required variables

---

## GitHub Repository Structure

Execution data writes to `ikwe-research` repo:

```
study-ii/
├── canonical-v1.0/        # LOCKED - do not touch
│   └── (research infrastructure)
│
└── execution-data/        # Written by this tool
    ├── index.json
    ├── scenarios/
    │   └── S2-XXX.json
    ├── runs/
    │   └── RUN-XXXX/
    │       └── raw.json
    └── exports/
        └── study_ii_export_YYYY-MM-DD.csv
```

---

## Notion Databases (Optional)

### StudyII_Scenarios

| Property | Type |
|----------|------|
| Scenario ID | Title |
| Case Source | Text |
| Harm Category | Select |
| Vulnerability Type | Select |
| Intensity | Number |
| Status | Select |
| GitHub Path | URL |
| Created | Date |

### StudyII_Runs

| Property | Type |
|----------|------|
| Run ID | Title |
| Scenario ID | Text |
| Model | Select |
| Condition | Select |
| Status | Select |
| Turns | Number |
| Scored | Checkbox |
| CF | Checkbox |
| Pathway | Select |
| GitHub Path | URL |
| Created | Date |

---

## Local Development

```bash
# Install Netlify CLI
npm install -g netlify-cli

# Install function dependencies
cd netlify/functions && npm install && cd ../..

# Run locally with Netlify Dev
netlify dev
```

Open `http://localhost:8888`

---

## Studies

| Study | Path | Status |
|-------|------|--------|
| Study II | `/study-ii` | Active |
| Study I | — | Completed (data locked) |
| Study III | `/study-iii` | Future |

Each study has isolated execution data but shares the runner infrastructure.

---

## Alignment with Canonical Infrastructure

This runner respects Study II v1.0 canonical lock:

- ✅ Does NOT modify `canonical-v1.0/` directory
- ✅ Writes ONLY to `execution-data/`
- ✅ Exports match Spreadsheet Schema v1.0
- ✅ Uses terminology from Scoring Codebook v1.0
- ✅ Every action creates audit trail in Git

---

© 2026 Ikwe.ai (Visible Healing Inc.)
