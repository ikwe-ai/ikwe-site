// Notion sync utility - mirrors metadata only
import { Client } from '@notionhq/client';

const notion = new Client({ auth: process.env.NOTION_API_KEY });

const SCENARIOS_DB = process.env.NOTION_SCENARIOS_DB;
const RUNS_DB = process.env.NOTION_RUNS_DB;

/**
 * Sync a scenario to Notion (create or update)
 */
export async function syncScenario(scenario) {
  if (!SCENARIOS_DB) {
    console.log('NOTION_SCENARIOS_DB not configured, skipping sync');
    return null;
  }
  
  try {
    // Check if exists
    const existing = await notion.databases.query({
      database_id: SCENARIOS_DB,
      filter: {
        property: 'Scenario ID',
        rich_text: { equals: scenario.scenario_id }
      }
    });
    
    const properties = {
      'Scenario ID': { title: [{ text: { content: scenario.scenario_id } }] },
      'Case Source': { rich_text: [{ text: { content: scenario.case_source_id || '' } }] },
      'Harm Category': { select: { name: scenario.harm_category || 'self-harm' } },
      'Vulnerability Type': { select: { name: scenario.vulnerability_type || 'ACUTE' } },
      'Intensity': { number: scenario.intensity_level || 3 },
      'Status': { select: { name: scenario.status || 'active' } },
      'GitHub Path': { url: `https://github.com/${process.env.GITHUB_REPO}/blob/main/study-ii/execution-data/scenarios/${scenario.scenario_id}.json` },
      'Created': { date: { start: scenario.created_at || new Date().toISOString() } }
    };
    
    if (existing.results.length > 0) {
      // Update
      return await notion.pages.update({
        page_id: existing.results[0].id,
        properties
      });
    } else {
      // Create
      return await notion.pages.create({
        parent: { database_id: SCENARIOS_DB },
        properties
      });
    }
  } catch (error) {
    console.error('Notion sync error (scenario):', error);
    return null;
  }
}

/**
 * Sync a run to Notion (create or update)
 */
export async function syncRun(run) {
  if (!RUNS_DB) {
    console.log('NOTION_RUNS_DB not configured, skipping sync');
    return null;
  }
  
  try {
    // Check if exists
    const existing = await notion.databases.query({
      database_id: RUNS_DB,
      filter: {
        property: 'Run ID',
        rich_text: { equals: run.run_id }
      }
    });
    
    const properties = {
      'Run ID': { title: [{ text: { content: run.run_id } }] },
      'Scenario ID': { rich_text: [{ text: { content: run.scenario_id } }] },
      'Model': { select: { name: run.model } },
      'Condition': { select: { name: run.condition || 'baseline' } },
      'Status': { select: { name: run.status || 'pending' } },
      'Turns': { number: run.turns?.length || 0 },
      'Scored': { checkbox: run.scored || false },
      'GitHub Path': { url: `https://github.com/${process.env.GITHUB_REPO}/tree/main/study-ii/execution-data/runs/${run.run_id}` },
      'Created': { date: { start: run.created_at || new Date().toISOString() } }
    };
    
    // Add CF result if scored
    if (run.cf_result !== undefined) {
      properties['CF'] = { checkbox: run.cf_result === 1 };
    }
    if (run.pathway) {
      properties['Pathway'] = { select: { name: run.pathway } };
    }
    
    if (existing.results.length > 0) {
      return await notion.pages.update({
        page_id: existing.results[0].id,
        properties
      });
    } else {
      return await notion.pages.create({
        parent: { database_id: RUNS_DB },
        properties
      });
    }
  } catch (error) {
    console.error('Notion sync error (run):', error);
    return null;
  }
}

/**
 * Get study stats from Notion
 */
export async function getStats() {
  if (!RUNS_DB) {
    return null;
  }
  
  try {
    const runs = await notion.databases.query({
      database_id: RUNS_DB
    });
    
    const total = runs.results.length;
    const completed = runs.results.filter(r => 
      r.properties.Status?.select?.name === 'completed'
    ).length;
    const scored = runs.results.filter(r => 
      r.properties.Scored?.checkbox === true
    ).length;
    
    return { total, completed, scored };
  } catch (error) {
    console.error('Notion stats error:', error);
    return null;
  }
}
