// Health check endpoint
import { corsHeaders, handleOptions, success } from './utils/auth.js';

export async function handler(event) {
  if (event.httpMethod === 'OPTIONS') {
    return handleOptions();
  }
  
  const status = {
    status: 'ok',
    timestamp: new Date().toISOString(),
    version: '1.0.0',
    study: 'Study II v1.0 CANONICAL',
    apis: {
      anthropic: !!process.env.ANTHROPIC_API_KEY,
      openai: !!process.env.OPENAI_API_KEY,
      google: !!process.env.GOOGLE_API_KEY,
      github: !!process.env.GITHUB_TOKEN,
      notion: !!process.env.NOTION_API_KEY
    }
  };
  
  return success(status);
}
