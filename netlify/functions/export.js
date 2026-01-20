// Export function - generates CSV matching Study II spreadsheet schema
import { corsHeaders, handleOptions, success, error, timestamp } from './utils/auth.js';
import { getIndex, readFile, writeFile, PATHS } from './utils/github.js';

export async function handler(event, context) {
  if (event.httpMethod === 'OPTIONS') {
    return handleOptions();
  }
  
  const user = context.clientContext?.user;
  if (!user) {
    return {
      statusCode: 401,
      headers: corsHeaders,
      body: JSON.stringify({ error: 'Authentication required' })
    };
  }
  
  if (event.httpMethod !== 'GET') {
    return error('Method not allowed', 405);
  }
  
  try {
    const index = await getIndex();
    const runs = index.runs || [];
    const scenarios = index.scenarios || [];
    
    // Build scenario lookup
    const scenarioMap = {};
    for (const s of scenarios) {
      const full = await readFile(`${PATHS.scenarios}/${s.scenario_id}.json`);
      if (full) {
        scenarioMap[s.scenario_id] = full.content;
      }
    }
    
    // CSV headers matching Study II Spreadsheet Schema v1.0
    const headers = [
      'Response_ID',
      'Scenario_ID',
      'Model_ID',
      'Coder_ID',
      'Coding_Date',
      'Vulnerability_Type',
      'Intensity_Level',
      'Explicit_Distress',
      'Support_Seeking',
      'SSF1_Premature_Solution',
      'SSF2_Minimization',
      'SSF3_Toxic_Positivity',
      'SSF4_Premature_Referral',
      'SSF5_Interrogation',
      'SSF6_Experience_Hijacking',
      'SSF7_Dismissive_Closure',
      'SSF_Count',
      'SSF_Any',
      'Harm_Indicator',
      'Repair_Level',
      'Repair_Notes',
      'CF',
      'CF_Reason',
      'Pathway',
      'Pathway_Notes',
      'Num_Turns',
      'Turn_at_CF',
      'Escalation',
      'Validation_Flag',
      'Needs_Review',
      'Review_Notes'
    ];
    
    // Build rows
    const rows = [];
    
    for (const runMeta of runs) {
      // Get full run data
      const runResult = await readFile(`${PATHS.runs}/${runMeta.run_id}/raw.json`);
      if (!runResult) continue;
      
      const run = runResult.content;
      const scenario = scenarioMap[run.scenario_id] || {};
      
      const row = {
        Response_ID: run.run_id,
        Scenario_ID: run.scenario_id,
        Model_ID: run.model,
        Coder_ID: '',
        Coding_Date: '',
        Vulnerability_Type: scenario.vulnerability_type || '',
        Intensity_Level: scenario.intensity_level || '',
        Explicit_Distress: scenario.explicit_distress || '',
        Support_Seeking: scenario.support_seeking || '',
        SSF1_Premature_Solution: '',
        SSF2_Minimization: '',
        SSF3_Toxic_Positivity: '',
        SSF4_Premature_Referral: '',
        SSF5_Interrogation: '',
        SSF6_Experience_Hijacking: '',
        SSF7_Dismissive_Closure: '',
        SSF_Count: '',
        SSF_Any: '',
        Harm_Indicator: '',
        Repair_Level: '',
        Repair_Notes: '',
        CF: '',
        CF_Reason: '',
        Pathway: run.pathway || '',
        Pathway_Notes: '',
        Num_Turns: run.turns?.length || 0,
        Turn_at_CF: '',
        Escalation: '',
        Validation_Flag: '',
        Needs_Review: '',
        Review_Notes: ''
      };
      
      // Pre-fill if scoring data exists
      if (run.ssf_flags) {
        row.SSF1_Premature_Solution = run.ssf_flags.ssf1 || '';
        row.SSF2_Minimization = run.ssf_flags.ssf2 || '';
        row.SSF3_Toxic_Positivity = run.ssf_flags.ssf3 || '';
        row.SSF4_Premature_Referral = run.ssf_flags.ssf4 || '';
        row.SSF5_Interrogation = run.ssf_flags.ssf5 || '';
        row.SSF6_Experience_Hijacking = run.ssf_flags.ssf6 || '';
        row.SSF7_Dismissive_Closure = run.ssf_flags.ssf7 || '';
      }
      
      if (run.cf_result !== undefined) {
        row.CF = run.cf_result;
      }
      
      rows.push(row);
    }
    
    // Generate CSV
    const csvLines = [headers.join(',')];
    
    for (const row of rows) {
      const values = headers.map(h => {
        const val = row[h];
        if (val === null || val === undefined) return '';
        // Escape quotes and wrap in quotes if contains comma
        const str = String(val);
        if (str.includes(',') || str.includes('"') || str.includes('\n')) {
          return `"${str.replace(/"/g, '""')}"`;
        }
        return str;
      });
      csvLines.push(values.join(','));
    }
    
    const csv = csvLines.join('\n');
    const exportTimestamp = timestamp().replace(/[:.]/g, '-');
    const filename = `study_ii_export_${exportTimestamp}.csv`;
    
    // Save to GitHub for audit trail
    await writeFile(
      `${PATHS.exports}/${filename}`,
      csv,
      `Export scoring data: ${filename}`
    );
    
    // Return CSV
    return {
      statusCode: 200,
      headers: {
        ...corsHeaders,
        'Content-Type': 'text/csv',
        'Content-Disposition': `attachment; filename="${filename}"`
      },
      body: csv
    };
    
  } catch (err) {
    console.error('Export error:', err);
    return error(err.message);
  }
}
