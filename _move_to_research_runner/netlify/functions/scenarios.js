// Scenarios API - GET and POST
import { corsHeaders, handleOptions, success, error, generateId, timestamp } from './utils/auth.js';
import { readFile, writeFile, listDirectory, PATHS, getIndex, updateIndex } from './utils/github.js';
import { syncScenario } from './utils/notion.js';

export async function handler(event, context) {
  if (event.httpMethod === 'OPTIONS') {
    return handleOptions();
  }
  
  // Check authentication via Netlify Identity
  const user = context.clientContext?.user;
  if (!user) {
    return {
      statusCode: 401,
      headers: corsHeaders,
      body: JSON.stringify({ error: 'Authentication required' })
    };
  }
  
  try {
    if (event.httpMethod === 'GET') {
      // List all scenarios
      const index = await getIndex();
      return success(index.scenarios || []);
    }
    
    if (event.httpMethod === 'POST') {
      const data = JSON.parse(event.body);
      
      // Generate ID
      const scenarioId = generateId('S2');
      
      const scenario = {
        scenario_id: scenarioId,
        case_source_id: data.case_source_id || '',
        harm_category: data.harm_category || 'self-harm',
        vulnerability_type: data.vulnerability_type || 'ACUTE',
        intensity_level: data.intensity_level || 3,
        explicit_distress: data.explicit_distress || 'YES',
        support_seeking: data.support_seeking || 'YES',
        context: data.context || '',
        user_turns: data.user_turns || [],
        created_at: timestamp(),
        created_by: user.email,
        status: 'active'
      };
      
      // Write to GitHub
      await writeFile(
        `${PATHS.scenarios}/${scenarioId}.json`,
        scenario,
        `Add scenario ${scenarioId}`
      );
      
      // Update index
      const index = await getIndex();
      index.scenarios = index.scenarios || [];
      index.scenarios.push({
        scenario_id: scenarioId,
        case_source_id: scenario.case_source_id,
        harm_category: scenario.harm_category,
        vulnerability_type: scenario.vulnerability_type,
        status: scenario.status,
        created_at: scenario.created_at
      });
      await updateIndex(index);
      
      // Sync to Notion (non-blocking)
      syncScenario(scenario).catch(console.error);
      
      return success({ success: true, scenario });
    }
    
    return error('Method not allowed', 405);
    
  } catch (err) {
    console.error('Scenarios error:', err);
    return error(err.message);
  }
}
