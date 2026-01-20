// GitHub append-only storage utility
import { Octokit } from 'octokit';

const octokit = new Octokit({ auth: process.env.GITHUB_TOKEN });
const REPO = process.env.GITHUB_REPO || 'ikwe-ai/ikwe-research';
const [OWNER, REPO_NAME] = REPO.split('/');

/**
 * Read a file from GitHub
 */
export async function readFile(path) {
  try {
    const response = await octokit.rest.repos.getContent({
      owner: OWNER,
      repo: REPO_NAME,
      path
    });
    
    if (response.data.type !== 'file') {
      throw new Error('Path is not a file');
    }
    
    const content = Buffer.from(response.data.content, 'base64').toString('utf-8');
    return {
      content: JSON.parse(content),
      sha: response.data.sha
    };
  } catch (error) {
    if (error.status === 404) {
      return null;
    }
    throw error;
  }
}

/**
 * Write a file to GitHub (create only - never overwrite without explicit sha)
 */
export async function writeFile(path, content, message, sha = null) {
  const contentBase64 = Buffer.from(
    typeof content === 'string' ? content : JSON.stringify(content, null, 2)
  ).toString('base64');
  
  const params = {
    owner: OWNER,
    repo: REPO_NAME,
    path,
    message,
    content: contentBase64
  };
  
  if (sha) {
    params.sha = sha;
  }
  
  const response = await octokit.rest.repos.createOrUpdateFileContents(params);
  return response.data;
}

/**
 * Append to a JSON array file (or create if doesn't exist)
 */
export async function appendToArray(path, item, message) {
  const existing = await readFile(path);
  
  let array = [];
  let sha = null;
  
  if (existing) {
    array = existing.content;
    sha = existing.sha;
  }
  
  array.push(item);
  
  return writeFile(path, array, message, sha);
}

/**
 * List files in a directory
 */
export async function listDirectory(path) {
  try {
    const response = await octokit.rest.repos.getContent({
      owner: OWNER,
      repo: REPO_NAME,
      path
    });
    
    if (!Array.isArray(response.data)) {
      return [];
    }
    
    return response.data.map(item => ({
      name: item.name,
      path: item.path,
      type: item.type,
      sha: item.sha
    }));
  } catch (error) {
    if (error.status === 404) {
      return [];
    }
    throw error;
  }
}

/**
 * Check if a path exists
 */
export async function exists(path) {
  try {
    await octokit.rest.repos.getContent({
      owner: OWNER,
      repo: REPO_NAME,
      path
    });
    return true;
  } catch (error) {
    if (error.status === 404) {
      return false;
    }
    throw error;
  }
}

// Study II specific paths
export const PATHS = {
  scenarios: 'study-ii/execution-data/scenarios',
  runs: 'study-ii/execution-data/runs',
  exports: 'study-ii/execution-data/exports',
  index: 'study-ii/execution-data/index.json'
};

/**
 * Get the execution data index
 */
export async function getIndex() {
  const result = await readFile(PATHS.index);
  if (!result) {
    return {
      scenarios: [],
      runs: [],
      lastUpdated: null
    };
  }
  return result.content;
}

/**
 * Update the execution data index
 */
export async function updateIndex(index) {
  index.lastUpdated = new Date().toISOString();
  const existing = await readFile(PATHS.index);
  return writeFile(
    PATHS.index,
    index,
    `Update execution index: ${index.lastUpdated}`,
    existing?.sha
  );
}
