# Study II Execution Tool — Setup Guide

**Version:** 1.0  
**Status:** Aligned with v1.0 Canonical Infrastructure

---

## Quick Start

### Step 1: Install Dependencies

```bash
pip3 install flask flask-cors anthropic openai google-generativeai
```

### Step 2: Set API Keys

```bash
# Required for Claude models
export ANTHROPIC_API_KEY='sk-ant-...'

# Optional for GPT models
export OPENAI_API_KEY='sk-proj-...'

# Optional for Gemini models  
export GOOGLE_API_KEY='AI...'
```

### Step 3: Start Backend

```bash
python3 study_ii_backend.py
```

You should see:
```
============================================================
🔬 Study II Execution Backend
   Mechanism-Based CF Analysis
============================================================

📊 API Status:
   Anthropic: ✅ Ready
   OpenAI:    ✅ Ready
   Google:    ✅ Ready

📁 Data directory: /path/to/study_ii_data

🌐 Server: http://localhost:5002
============================================================
```

### Step 4: Open Frontend

Open `study_ii_frontend.html` in your browser.

---

## Workflow

### 1. Add Scenarios

Click "+ Add" to create abstracted scenarios from public cases:

- **Case Source ID**: Reference to original public case
- **Harm Category**: self-harm, crisis, vulnerability
- **Vulnerability Type**: ACUTE, CHRONIC, TRANSITIONAL
- **Intensity Level**: 1-5 scale
- **User Turns**: The messages that will be sent to models

### 2. Run Tests

For each scenario:

1. Select the scenario in the sidebar
2. Click "▶ Run" next to each model you want to test
3. The tool automatically:
   - Creates a run record
   - Sends each user turn to the model
   - Captures the model's responses
   - Saves the complete conversation

### 3. Export for Scoring

Click "📊 Export for Scoring" to download a CSV that matches the locked spreadsheet schema:

- Pre-filled: Response_ID, Scenario_ID, Model_ID, scenario characteristics
- Empty (for manual scoring): SSF columns, Repair_Level, Pathway, etc.

### 4. Score Using Codebook

1. Import the CSV into the scoring spreadsheet template
2. Use the Scoring Codebook v1.0 decision trees to fill in:
   - SSF1-SSF7 (0 or 1 each)
   - Harm_Indicator (YES/NO/N/A)
   - Repair_Level (R-A, R-I, R-0, N/A)
3. CF and CF_Reason auto-calculate
4. If CF=1, classify Pathway (A, B, C, OTHER)

---

## Data Storage

All data is stored locally in `study_ii_data/`:

```
study_ii_data/
├── scenarios.json     # All scenario definitions
├── responses.json     # (reserved for future use)
├── runs.json          # All test runs with conversations
└── exports/           # Generated export files
```

---

## API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/health` | GET | Check server and API status |
| `/api/scenarios` | GET | List all scenarios |
| `/api/scenarios` | POST | Add new scenario |
| `/api/scenarios/<id>` | PUT | Update scenario |
| `/api/runs` | GET | List all runs |
| `/api/runs` | POST | Create new run |
| `/api/runs/<id>` | PUT | Update run |
| `/api/runs/<id>/turn` | POST | Add turn to run |
| `/api/fetch` | POST | Fetch response from model |
| `/api/export/spreadsheet` | GET | Export CSV for scoring |
| `/api/export/full` | GET | Export complete JSON |
| `/api/stats` | GET | Get execution statistics |

---

## Models Supported

| Model ID | Name | API |
|----------|------|-----|
| `claude-sonnet` | Claude Sonnet 4 | Anthropic |
| `claude-opus` | Claude Opus 4 | Anthropic |
| `gpt-4o` | GPT-4o | OpenAI |
| `gpt-4-turbo` | GPT-4 Turbo | OpenAI |
| `gemini-pro` | Gemini 1.5 Pro | Google |
| `gemini-flash` | Gemini 1.5 Flash | Google |

---

## Alignment with Canonical Infrastructure

This tool produces data that maps directly to:

- **Scoring Spreadsheet Schema v1.0** — Export format matches column structure
- **Scoring Codebook v1.0** — UI labels match codebook terminology
- **CF Definition v1.0** — Data structure supports CF computation

**Important**: The tool collects responses only. CF scoring must be done manually using the locked codebook to maintain research integrity.

---

## Troubleshooting

### "Backend not running"
- Make sure `python3 study_ii_backend.py` is running in a terminal
- Check the terminal for error messages

### "API not configured"
- Verify environment variables are set: `echo $ANTHROPIC_API_KEY`
- Keys must be set in the same terminal session as the backend

### "Model error"
- Check API key has sufficient credits
- Some models may have rate limits

---

## Next Steps After Data Collection

1. Export all runs: `📊 Export for Scoring`
2. Import into scoring spreadsheet template
3. Score each run using Scoring Codebook v1.0
4. Verify CF formulas calculate correctly
5. Run aggregation for Results section
