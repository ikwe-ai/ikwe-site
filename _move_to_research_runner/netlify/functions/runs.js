// Runs API - GET, POST, PUT
import { corsHeaders, handleOptions, success, error, generateId, timestamp } from './utils/auth.js';
import { readFile, writeFile, PATHS, getIndex, updateIndex } from './utils/github.js';
import { syncRun } from './utils/notion.js';

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
    // Parse path for run ID
    const pathParts = event.path.split('/').filter(Boolean);
    const runId = pathParts.length > 2 ? pathParts[2] : null;
    const action = pathParts.length > 3 ? pathParts[3] : null;
    
    if (event.httpMethod === 'GET') {
      if (runId) {
        // Get specific run
        const result = await readFile(`${PATHS.runs}/${runId}/raw.json`);
        if (!result) {
          return error('Run not found', 404);
        }
        return success(result.content);
      } else {
        // List all runs
        const index = await getIndex();
        return success(index.runs || []);
      }
    }
    
    if (event.httpMethod === 'POST') {
      const data = JSON.parse(event.body);
      
      // Handle turn addition
      if (runId && action === 'turn') {
        const result = await readFile(`${PATHS.runs}/${runId}/raw.json`);
        if (!result) {
          return error('Run not found', 404);
        }
        
        const run = result.content;
        run.turns = run.turns || [];
        
        const turn = {
          turn_idx: run.turns.length + 1,
          user_content: data.user_content || '',
          assistant_content: data.assistant_content || '',
          timestamp: timestamp()
        };
        
        run.turns.push(turn);
        run.updated_at = timestamp();
        
        await writeFile(
          `${PATHS.runs}/${runId}/raw.json`,
          run,
          `Add turn ${turn.turn_idx} to ${runId}`,
          result.sha
        );
        
        // Update Notion
        syncRun(run).catch(console.error);
        
        return success({ success: true, turn });
      }
      
      // Create new run
      const newRunId = generateId('RUN');
      
      const run = {
        run_id: newRunId,
        scenario_id: data.scenario_id,
        model: data.model,
        condition: data.condition || 'baseline',
        run_num: data.run_num || 1,
        turns: [],
        created_at: timestamp(),
        created_by: user.email,
        status: 'pending',
        scored: false
      };
      
      // Write to GitHub
      await writeFile(
        `${PATHS.runs}/${newRunId}/raw.json`,
        run,
        `Create run ${newRunId}`
      );
      
      // Update index
      const index = await getIndex();
      index.runs = index.runs || [];
      index.runs.push({
        run_id: newRunId,
        scenario_id: run.scenario_id,
        model: run.model,
        condition: run.condition,
        status: run.status,
        created_at: run.created_at
      });
      await updateIndex(index);
      
      // Sync to Notion
      syncRun(run).catch(console.error);
      
      return success({ success: true, run });
    }
    
    if (event.httpMethod === 'PUT' && runId) {
      const data = JSON.parse(event.body);
      
      const result = await readFile(`${PATHS.runs}/${runId}/raw.json`);
      if (!result) {
        return error('Run not found', 404);
      }
      
      const run = result.content;
      
      // Update allowed fields
      if (data.status) run.status = data.status;
      if (data.scored !== undefined) run.scored = data.scored;
      if (data.cf_result !== undefined) run.cf_result = data.cf_result;
      if (data.pathway) run.pathway = data.pathway;
      if (data.ssf_flags) run.ssf_flags = data.ssf_flags;
      if (data.notes) run.notes = data.notes;
      
      run.updated_at = timestamp();
      run.updated_by = user.email;
      
      await writeFile(
        `${PATHS.runs}/${runId}/raw.json`,
        run,
        `Update run ${runId}: ${data.status || 'metadata'}`,
        result.sha
      );
      
      // Update index
      const index = await getIndex();
      const runIndex = index.runs?.findIndex(r => r.run_id === runId);
      if (runIndex >= 0) {
        index.runs[runIndex].status = run.status;
        index.runs[runIndex].scored = run.scored;
        await updateIndex(index);
      }
      
      // Sync to Notion
      syncRun(run).catch(console.error);
      
      return success({ success: true, run });
    }
    
    return error('Method not allowed', 405);
    
  } catch (err) {
    console.error('Runs error:', err);
    return error(err.message);
  }
}
