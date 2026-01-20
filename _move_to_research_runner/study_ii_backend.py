#!/usr/bin/env python3
"""
Study II Execution Backend
Mechanism-Based Analysis of Catastrophic Failure in AI Emotional Safety

This backend:
1. Serves abstracted scenarios to models
2. Fetches responses from frontier AI models
3. Stores responses for manual CF scoring
4. Exports data in format matching the locked spreadsheet schema
"""

from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
import os
import json
import csv
from datetime import datetime
from pathlib import Path

# API client imports
try:
    import anthropic
    HAS_ANTHROPIC = True
except ImportError:
    HAS_ANTHROPIC = False

try:
    import openai
    HAS_OPENAI = True
except ImportError:
    HAS_OPENAI = False

try:
    import google.generativeai as genai
    HAS_GOOGLE = True
except ImportError:
    HAS_GOOGLE = False

app = Flask(__name__)
CORS(app)

# ========================================
# CONFIGURATION
# ========================================

DATA_DIR = Path("study_ii_data")
DATA_DIR.mkdir(exist_ok=True)

SCENARIOS_FILE = DATA_DIR / "scenarios.json"
RESPONSES_FILE = DATA_DIR / "responses.json"
RUNS_FILE = DATA_DIR / "runs.json"

# Models to test (aligned with Study II methods)
MODELS = {
    "claude-sonnet": {
        "name": "Claude Sonnet 4",
        "api": "anthropic",
        "model_id": "claude-sonnet-4-20250514"
    },
    "claude-opus": {
        "name": "Claude Opus 4",
        "api": "anthropic", 
        "model_id": "claude-opus-4-20250514"
    },
    "gpt-4o": {
        "name": "GPT-4o",
        "api": "openai",
        "model_id": "gpt-4o"
    },
    "gpt-4-turbo": {
        "name": "GPT-4 Turbo",
        "api": "openai",
        "model_id": "gpt-4-turbo"
    },
    "gemini-pro": {
        "name": "Gemini Pro",
        "api": "google",
        "model_id": "gemini-1.5-pro"
    },
    "gemini-flash": {
        "name": "Gemini Flash",
        "api": "google",
        "model_id": "gemini-1.5-flash"
    }
}

# ========================================
# API CLIENTS
# ========================================

anthropic_client = None
openai_client = None

if HAS_ANTHROPIC and os.environ.get("ANTHROPIC_API_KEY"):
    anthropic_client = anthropic.Anthropic()
    
if HAS_OPENAI and os.environ.get("OPENAI_API_KEY"):
    openai_client = openai.OpenAI()

if HAS_GOOGLE and os.environ.get("GOOGLE_API_KEY"):
    genai.configure(api_key=os.environ.get("GOOGLE_API_KEY"))

# ========================================
# DATA PERSISTENCE
# ========================================

def load_json(filepath):
    if filepath.exists():
        with open(filepath) as f:
            return json.load(f)
    return []

def save_json(filepath, data):
    with open(filepath, 'w') as f:
        json.dump(data, f, indent=2, default=str)

def get_scenarios():
    return load_json(SCENARIOS_FILE)

def get_responses():
    return load_json(RESPONSES_FILE)

def get_runs():
    return load_json(RUNS_FILE)

def save_scenarios(scenarios):
    save_json(SCENARIOS_FILE, scenarios)

def save_responses(responses):
    save_json(RESPONSES_FILE, responses)

def save_runs(runs):
    save_json(RUNS_FILE, runs)

# ========================================
# API ENDPOINTS
# ========================================

@app.route('/api/health', methods=['GET'])
def health():
    """Check server and API status"""
    return jsonify({
        'status': 'ok',
        'timestamp': datetime.now().isoformat(),
        'apis': {
            'anthropic': anthropic_client is not None,
            'openai': openai_client is not None,
            'google': HAS_GOOGLE and os.environ.get("GOOGLE_API_KEY") is not None
        },
        'models_available': [
            model_id for model_id, config in MODELS.items()
            if (config['api'] == 'anthropic' and anthropic_client) or
               (config['api'] == 'openai' and openai_client) or
               (config['api'] == 'google' and HAS_GOOGLE)
        ]
    })

@app.route('/api/scenarios', methods=['GET'])
def list_scenarios():
    """List all scenarios"""
    return jsonify(get_scenarios())

@app.route('/api/scenarios', methods=['POST'])
def add_scenario():
    """Add a new scenario"""
    data = request.json
    scenarios = get_scenarios()
    
    scenario = {
        'scenario_id': f"S2-{len(scenarios) + 1:03d}",
        'case_source_id': data.get('case_source_id', ''),
        'harm_category': data.get('harm_category', 'self-harm'),
        'vulnerability_type': data.get('vulnerability_type', 'ACUTE'),
        'intensity_level': data.get('intensity_level', 3),
        'explicit_distress': data.get('explicit_distress', 'YES'),
        'support_seeking': data.get('support_seeking', 'YES'),
        'context': data.get('context', ''),
        'user_turns': data.get('user_turns', []),
        'created_at': datetime.now().isoformat(),
        'status': 'active'
    }
    
    scenarios.append(scenario)
    save_scenarios(scenarios)
    
    return jsonify({'success': True, 'scenario': scenario})

@app.route('/api/scenarios/<scenario_id>', methods=['PUT'])
def update_scenario(scenario_id):
    """Update a scenario"""
    data = request.json
    scenarios = get_scenarios()
    
    for i, s in enumerate(scenarios):
        if s['scenario_id'] == scenario_id:
            scenarios[i].update(data)
            save_scenarios(scenarios)
            return jsonify({'success': True, 'scenario': scenarios[i]})
    
    return jsonify({'error': 'Scenario not found'}), 404

@app.route('/api/fetch', methods=['POST'])
def fetch_response():
    """Fetch response from a specific model"""
    data = request.json
    model_id = data.get('model')
    messages = data.get('messages', [])
    
    if not model_id or model_id not in MODELS:
        return jsonify({'error': f'Unknown model: {model_id}'}), 400
    
    if not messages:
        return jsonify({'error': 'No messages provided'}), 400
    
    model_config = MODELS[model_id]
    
    try:
        if model_config['api'] == 'anthropic':
            if not anthropic_client:
                return jsonify({'error': 'Anthropic API not configured'}), 400
            
            response = anthropic_client.messages.create(
                model=model_config['model_id'],
                max_tokens=2000,
                messages=messages
            )
            return jsonify({
                'response': response.content[0].text,
                'model': model_id,
                'model_name': model_config['name']
            })
            
        elif model_config['api'] == 'openai':
            if not openai_client:
                return jsonify({'error': 'OpenAI API not configured'}), 400
            
            response = openai_client.chat.completions.create(
                model=model_config['model_id'],
                messages=messages,
                max_tokens=2000
            )
            return jsonify({
                'response': response.choices[0].message.content,
                'model': model_id,
                'model_name': model_config['name']
            })
            
        elif model_config['api'] == 'google':
            if not HAS_GOOGLE:
                return jsonify({'error': 'Google API not configured'}), 400
            
            model = genai.GenerativeModel(model_config['model_id'])
            # Convert messages to Gemini format
            prompt = "\n\n".join([
                f"{'User' if m['role'] == 'user' else 'Assistant'}: {m['content']}"
                for m in messages
            ])
            response = model.generate_content(prompt)
            return jsonify({
                'response': response.text,
                'model': model_id,
                'model_name': model_config['name']
            })
            
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/runs', methods=['GET'])
def list_runs():
    """List all runs"""
    return jsonify(get_runs())

@app.route('/api/runs', methods=['POST'])
def create_run():
    """Create a new run (scenario + model combination)"""
    data = request.json
    runs = get_runs()
    
    run = {
        'run_id': f"RUN-{len(runs) + 1:04d}",
        'scenario_id': data.get('scenario_id'),
        'model': data.get('model'),
        'condition': data.get('condition', 'baseline'),
        'run_num': data.get('run_num', 1),
        'turns': [],  # Will hold the conversation
        'created_at': datetime.now().isoformat(),
        'status': 'pending',
        'scored': False
    }
    
    runs.append(run)
    save_runs(runs)
    
    return jsonify({'success': True, 'run': run})

@app.route('/api/runs/<run_id>', methods=['PUT'])
def update_run(run_id):
    """Update a run with responses or scores"""
    data = request.json
    runs = get_runs()
    
    for i, r in enumerate(runs):
        if r['run_id'] == run_id:
            runs[i].update(data)
            runs[i]['updated_at'] = datetime.now().isoformat()
            save_runs(runs)
            return jsonify({'success': True, 'run': runs[i]})
    
    return jsonify({'error': 'Run not found'}), 404

@app.route('/api/runs/<run_id>/turn', methods=['POST'])
def add_turn(run_id):
    """Add a turn to a run"""
    data = request.json
    runs = get_runs()
    
    for i, r in enumerate(runs):
        if r['run_id'] == run_id:
            turn = {
                'turn_idx': len(r['turns']) + 1,
                'user_content': data.get('user_content', ''),
                'assistant_content': data.get('assistant_content', ''),
                'timestamp': datetime.now().isoformat()
            }
            runs[i]['turns'].append(turn)
            save_runs(runs)
            return jsonify({'success': True, 'turn': turn})
    
    return jsonify({'error': 'Run not found'}), 404

@app.route('/api/export/spreadsheet', methods=['GET'])
def export_spreadsheet():
    """Export runs in format matching Study II spreadsheet schema"""
    runs = get_runs()
    scenarios = {s['scenario_id']: s for s in get_scenarios()}
    
    # Build rows for the spreadsheet
    rows = []
    for run in runs:
        scenario = scenarios.get(run['scenario_id'], {})
        
        base_row = {
            'Response_ID': run['run_id'],
            'Scenario_ID': run['scenario_id'],
            'Model_ID': run['model'],
            'Coder_ID': '',
            'Coding_Date': '',
            'Vulnerability_Type': scenario.get('vulnerability_type', ''),
            'Intensity_Level': scenario.get('intensity_level', ''),
            'Explicit_Distress': scenario.get('explicit_distress', ''),
            'Support_Seeking': scenario.get('support_seeking', ''),
            'Num_Turns': len(run.get('turns', [])),
            'Condition': run.get('condition', 'baseline'),
            'Run_Num': run.get('run_num', 1)
        }
        
        # Add SSF columns (to be filled manually)
        for i in range(1, 8):
            base_row[f'SSF{i}'] = ''
        
        base_row['Harm_Indicator'] = ''
        base_row['Repair_Level'] = ''
        base_row['Pathway'] = ''
        base_row['Notes'] = ''
        
        rows.append(base_row)
    
    # Write CSV
    output_path = DATA_DIR / f"study_ii_export_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
    
    if rows:
        with open(output_path, 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=rows[0].keys())
            writer.writeheader()
            writer.writerows(rows)
    
    return send_file(output_path, as_attachment=True)

@app.route('/api/export/full', methods=['GET'])
def export_full():
    """Export complete data as JSON"""
    data = {
        'export_date': datetime.now().isoformat(),
        'scenarios': get_scenarios(),
        'runs': get_runs(),
        'study_version': 'Study II v1.0'
    }
    
    output_path = DATA_DIR / f"study_ii_full_export_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    save_json(output_path, data)
    
    return send_file(output_path, as_attachment=True)

@app.route('/api/stats', methods=['GET'])
def get_stats():
    """Get execution statistics"""
    runs = get_runs()
    scenarios = get_scenarios()
    
    # Count by model
    by_model = {}
    for run in runs:
        model = run.get('model', 'unknown')
        by_model[model] = by_model.get(model, 0) + 1
    
    # Count by status
    completed = sum(1 for r in runs if r.get('status') == 'completed')
    scored = sum(1 for r in runs if r.get('scored', False))
    
    return jsonify({
        'total_scenarios': len(scenarios),
        'total_runs': len(runs),
        'completed_runs': completed,
        'scored_runs': scored,
        'runs_by_model': by_model,
        'progress_pct': round(completed / max(len(runs), 1) * 100, 1)
    })

# ========================================
# MAIN
# ========================================

if __name__ == '__main__':
    print("\n" + "=" * 60)
    print("🔬 Study II Execution Backend")
    print("   Mechanism-Based CF Analysis")
    print("=" * 60)
    
    print("\n📊 API Status:")
    print(f"   Anthropic: {'✅ Ready' if anthropic_client else '❌ Not configured'}")
    print(f"   OpenAI:    {'✅ Ready' if openai_client else '❌ Not configured'}")
    print(f"   Google:    {'✅ Ready' if HAS_GOOGLE and os.environ.get('GOOGLE_API_KEY') else '❌ Not configured'}")
    
    print(f"\n📁 Data directory: {DATA_DIR.absolute()}")
    print(f"\n🌐 Server: http://localhost:5002")
    print("\n" + "=" * 60 + "\n")
    
    app.run(debug=True, host='0.0.0.0', port=5002)
