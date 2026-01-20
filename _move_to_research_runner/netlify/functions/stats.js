// Stats function - execution progress
import { corsHeaders, handleOptions, success, error } from './utils/auth.js';
import { getIndex } from './utils/github.js';
import { getStats as getNotionStats } from './utils/notion.js';

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
  
  try {
    const index = await getIndex();
    
    const scenarios = index.scenarios || [];
    const runs = index.runs || [];
    
    // Count by model
    const byModel = {};
    const byStatus = { pending: 0, completed: 0 };
    let scored = 0;
    
    for (const run of runs) {
      byModel[run.model] = (byModel[run.model] || 0) + 1;
      byStatus[run.status] = (byStatus[run.status] || 0) + 1;
      if (run.scored) scored++;
    }
    
    const stats = {
      total_scenarios: scenarios.length,
      total_runs: runs.length,
      completed_runs: byStatus.completed || 0,
      scored_runs: scored,
      runs_by_model: byModel,
      runs_by_status: byStatus,
      progress_pct: runs.length > 0 
        ? Math.round((byStatus.completed || 0) / runs.length * 100) 
        : 0,
      last_updated: index.lastUpdated
    };
    
    return success(stats);
    
  } catch (err) {
    console.error('Stats error:', err);
    return error(err.message);
  }
}
