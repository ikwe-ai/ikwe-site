// netlify/functions/inquiry.js
// Handles engagement inquiry form submissions

const { Client } = require('@notionhq/client');

const notion = new Client({
  auth: process.env.NOTION_API_KEY,
});

const DATABASE_ID = process.env.NOTION_INQUIRIES_DB;

exports.handler = async (event, context) => {
  // CORS headers
  const headers = {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Headers': 'Content-Type',
    'Access-Control-Allow-Methods': 'POST, OPTIONS',
  };

  // Handle preflight
  if (event.httpMethod === 'OPTIONS') {
    return { statusCode: 200, headers, body: '' };
  }

  if (event.httpMethod !== 'POST') {
    return { 
      statusCode: 405, 
      headers,
      body: JSON.stringify({ error: 'Method not allowed' }) 
    };
  }

  try {
    const data = JSON.parse(event.body);
    
    // Validate required fields
    const required = ['name', 'email', 'organization', 'role', 'product_description', 'product_stage', 'engagement_type', 'source'];
    for (const field of required) {
      if (!data[field]) {
        return {
          statusCode: 400,
          headers,
          body: JSON.stringify({ error: `Missing required field: ${field}` })
        };
      }
    }

    // Create Notion page
    const response = await notion.pages.create({
      parent: { database_id: DATABASE_ID },
      properties: {
        'Name': {
          title: [{ text: { content: data.name } }]
        },
        'Email': {
          email: data.email
        },
        'Organization': {
          rich_text: [{ text: { content: data.organization } }]
        },
        'Role': {
          rich_text: [{ text: { content: data.role } }]
        },
        'Product Description': {
          rich_text: [{ text: { content: data.product_description } }]
        },
        'Product Stage': {
          select: { name: data.product_stage }
        },
        'Engagement Type': {
          select: { name: data.engagement_type }
        },
        'Source': {
          select: { name: data.source }
        },
        'Details': {
          rich_text: [{ text: { content: data.details || '' } }]
        },
        'Status': {
          select: { name: 'New' }
        },
        'Submitted': {
          date: { start: new Date().toISOString() }
        }
      }
    });

    return {
      statusCode: 200,
      headers,
      body: JSON.stringify({ 
        success: true, 
        message: 'Inquiry submitted successfully',
        id: response.id 
      })
    };

  } catch (error) {
    console.error('Error creating Notion page:', error);
    
    return {
      statusCode: 500,
      headers,
      body: JSON.stringify({ 
        error: 'Failed to submit inquiry',
        details: error.message 
      })
    };
  }
};
