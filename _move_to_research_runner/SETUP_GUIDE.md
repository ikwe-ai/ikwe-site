# research.ikwe.ai — Complete Setup Guide

This guide walks you through setting up your secure research portal from scratch.

---

## Prerequisites

- GitHub account with a repository for `ikwe-research`
- Netlify account
- Domain DNS access (for `research.ikwe.ai` subdomain)
- API keys for models you want to test

---

## Step 1: Prepare GitHub Repository

### 1.1 Create execution data structure

In your `ikwe-research` repo, create:

```
study-ii/
└── execution-data/
    ├── index.json
    ├── scenarios/
    │   └── .gitkeep
    ├── runs/
    │   └── .gitkeep
    └── exports/
        └── .gitkeep
```

Initial `index.json`:
```json
{
  "scenarios": [],
  "runs": [],
  "lastUpdated": null
}
```

### 1.2 Create GitHub Personal Access Token

1. Go to GitHub → Settings → Developer settings → Personal access tokens → Fine-grained tokens
2. Create new token:
   - Name: `ikwe-research-runner`
   - Repository access: Select `ikwe-research`
   - Permissions: Contents (Read and write)
3. Copy the token

---

## Step 2: Deploy to Netlify

### 2.1 Create new Netlify site

Option A — Via CLI:
```bash
cd ikwe-research-runner
netlify init
# Choose: Create & configure a new site
# Team: Your team
# Site name: ikwe-research (or similar)
```

Option B — Via Dashboard:
1. Go to app.netlify.com
2. Add new site → Import an existing project
3. Connect to your repo containing this folder

### 2.2 Deploy

```bash
netlify deploy --prod
```

Or push to the connected Git branch.

---

## Step 3: Configure Custom Domain

### 3.1 In Netlify Dashboard

1. Site settings → Domain management
2. Add custom domain: `research.ikwe.ai`
3. Note the Netlify domain (e.g., `ikwe-research.netlify.app`)

### 3.2 In Your DNS Provider

Add a CNAME record:
```
Type: CNAME
Name: research
Value: ikwe-research.netlify.app
TTL: Auto
```

Wait 5-30 minutes for propagation.

### 3.3 Enable HTTPS

Netlify will auto-provision SSL. Verify at:
- Site settings → Domain management → HTTPS

---

## Step 4: Enable Authentication

### 4.1 Enable Netlify Identity

1. Site settings → Identity → Enable Identity
2. Registration preferences: **Invite only**
3. External providers: Disable all (email-only is fine)

### 4.2 Invite Yourself

1. Identity tab → Invite users
2. Enter your email
3. Check email, set password

---

## Step 5: Set Environment Variables

In Netlify Dashboard → Site settings → Environment variables:

### Required

| Variable | Value | Notes |
|----------|-------|-------|
| `ANTHROPIC_API_KEY` | `sk-ant-...` | For Claude models |
| `GITHUB_TOKEN` | `ghp_...` | From Step 1.2 |
| `GITHUB_REPO` | `ikwe-ai/ikwe-research` | Your repo path |

### Optional (for additional models)

| Variable | Value | Notes |
|----------|-------|-------|
| `OPENAI_API_KEY` | `sk-proj-...` | For GPT models |
| `GOOGLE_API_KEY` | `AI...` | For Gemini models |

### Optional (for Notion sync)

| Variable | Value | Notes |
|----------|-------|-------|
| `NOTION_API_KEY` | `secret_...` | Integration token |
| `NOTION_SCENARIOS_DB` | `abc123...` | Database ID |
| `NOTION_RUNS_DB` | `def456...` | Database ID |

After adding variables, **redeploy** the site.

---

## Step 6: Set Up Notion (Optional)

### 6.1 Create Integration

1. Go to notion.so/my-integrations
2. Create new integration: `ikwe-research-runner`
3. Copy the Internal Integration Token

### 6.2 Create Databases

Create two databases with these schemas:

**StudyII_Scenarios:**
- Scenario ID (Title)
- Case Source (Text)
- Harm Category (Select: self-harm, crisis, vulnerability)
- Vulnerability Type (Select: ACUTE, CHRONIC, TRANSITIONAL)
- Intensity (Number)
- Status (Select: active, archived)
- GitHub Path (URL)
- Created (Date)

**StudyII_Runs:**
- Run ID (Title)
- Scenario ID (Text)
- Model (Select: claude-sonnet, claude-opus, gpt-4o, etc.)
- Condition (Select: baseline, eq_safety)
- Status (Select: pending, completed)
- Turns (Number)
- Scored (Checkbox)
- CF (Checkbox)
- Pathway (Select: A, B, C, OTHER)
- GitHub Path (URL)
- Created (Date)

### 6.3 Share with Integration

For each database:
1. Click ... → Add connections
2. Select your integration
3. Confirm

### 6.4 Get Database IDs

Open each database as a full page. The URL looks like:
```
https://notion.so/workspace/DATABASE_ID?v=...
```

Copy the DATABASE_ID (32-character string).

---

## Step 7: Verify Setup

### 7.1 Visit research.ikwe.ai

You should see the login gate.

### 7.2 Log In

Use the credentials from your invite email.

### 7.3 Check API Status

After logging in, the status bar should show:
- Green dot
- "Connected: Claude, GPT, Gemini" (depending on keys set)

### 7.4 Test Scenario Creation

1. Click "+ Add"
2. Fill in a test scenario
3. Save
4. Check GitHub: `study-ii/execution-data/scenarios/` should have a new file
5. Check Notion: StudyII_Scenarios should have a new row

### 7.5 Test Model Run

1. Select your test scenario
2. Click "▶ Run" next to a model
3. Watch the toast notifications
4. Check the "Runs" tab for the new run
5. Verify in GitHub: `study-ii/execution-data/runs/RUN-XXX/raw.json`

---

## Troubleshooting

### "Authentication required" errors

- Verify you're logged in (check Identity widget)
- Try logging out and back in
- Check browser console for JWT errors

### "GitHub API not configured"

- Verify GITHUB_TOKEN is set correctly
- Token must have write access to the repo
- Redeploy after changing env vars

### "Model API not configured"

- Verify the relevant API key is set
- Keys are case-sensitive
- Redeploy after changes

### Notion not syncing

- Verify NOTION_API_KEY is correct
- Verify database IDs are correct
- Check that databases are shared with integration
- Notion sync is non-blocking; GitHub writes still work

---

## Daily Workflow

1. **Log in** at research.ikwe.ai
2. **Add scenarios** abstracted from public cases
3. **Run tests** across models (baseline condition)
4. **Export** to CSV for manual scoring
5. **Score** using Codebook v1.0 and spreadsheet template
6. **Update** run records with CF results (optional)

All data is preserved in GitHub with full audit trail.

---

## Security Checklist

- [ ] Netlify Identity is invite-only
- [ ] Only you (and trusted researchers) have accounts
- [ ] GitHub token has minimal required permissions
- [ ] API keys are in environment variables, not code
- [ ] HTTPS is enabled
- [ ] No sensitive data in client-side code

---

You're ready to run Study II with full audit trail and security.
