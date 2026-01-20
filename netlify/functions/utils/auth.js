// Shared authentication and utility functions

/**
 * Verify Netlify Identity JWT token
 * Returns user object if valid, null if not
 */
export function verifyAuth(event) {
  const authHeader = event.headers.authorization;
  
  if (!authHeader || !authHeader.startsWith('Bearer ')) {
    return null;
  }
  
  // Netlify Identity provides user context automatically
  // when using identity-aware functions
  const context = event.context || {};
  const clientContext = context.clientContext || {};
  const user = clientContext.user;
  
  return user || null;
}

/**
 * Standard CORS headers
 */
export const corsHeaders = {
  'Access-Control-Allow-Origin': '*',
  'Access-Control-Allow-Headers': 'Content-Type, Authorization',
  'Access-Control-Allow-Methods': 'GET, POST, PUT, OPTIONS',
  'Content-Type': 'application/json'
};

/**
 * Handle OPTIONS preflight
 */
export function handleOptions() {
  return {
    statusCode: 200,
    headers: corsHeaders,
    body: ''
  };
}

/**
 * Return 401 Unauthorized
 */
export function unauthorized() {
  return {
    statusCode: 401,
    headers: corsHeaders,
    body: JSON.stringify({ error: 'Authentication required' })
  };
}

/**
 * Return success response
 */
export function success(data) {
  return {
    statusCode: 200,
    headers: corsHeaders,
    body: JSON.stringify(data)
  };
}

/**
 * Return error response
 */
export function error(message, statusCode = 500) {
  return {
    statusCode,
    headers: corsHeaders,
    body: JSON.stringify({ error: message })
  };
}

/**
 * Generate timestamp-based ID
 */
export function generateId(prefix) {
  const timestamp = Date.now().toString(36);
  const random = Math.random().toString(36).substring(2, 6);
  return `${prefix}-${timestamp}-${random}`.toUpperCase();
}

/**
 * Get current ISO timestamp
 */
export function timestamp() {
  return new Date().toISOString();
}
