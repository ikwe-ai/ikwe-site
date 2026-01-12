// netlify/functions/access-request.js
// Handles research report access requests and adds to Notion database

const { Client } = require('@notionhq/client');

const notion = new Client({ auth: process.env.NOTION_API_KEY });
const databaseId = process.env.NOTION_ACCESS_DB_ID;

exports.handler = async (event) => {
  if (event.httpMethod !== 'POST') {
    return {
      statusCode: 405,
      body: JSON.stringify({ error: 'Method not allowed' })
    };
  }

  try {
    const {
      name,
      email,
      organization,
      role,
      intended_use,
      description
    } = JSON.parse(event.body);

    if (!name || !email || !organization) {
      return {
        statusCode: 400,
        body: JSON.stringify({ error: 'Name, email, and organization are required' })
      };
    }

    await notion.pages.create({
      parent: { database_id: databaseId },
      properties: {
        Name: {
          title: [{ text: { content: name } }]
        },
        Email: {
          email: email
        },
        Organization: {
          rich_text: [{ text: { content: organization } }]
        },
        Role: {
          rich_text: [{ text: { content: role || '' } }]
        },
        'Intended Use': {
          select: intended_use ? { name: intended_use } : null
        },
        Description: {
          rich_text: [{ text: { content: description || '' } }]
        },
        Status: {
          select: { name: 'Pending' }
        },
        'Requested At': {
          date: { start: new Date().toISOString() }
        }
      }
    });

    return {
      statusCode: 200,
      body: JSON.stringify({ success: true, message: 'Access request submitted successfully' })
    };

  } catch (error) {
    console.error('Access request error:', error);
    return {
      statusCode: 500,
      body: JSON.stringify({ error: 'Request failed' })
    };
  }
};
