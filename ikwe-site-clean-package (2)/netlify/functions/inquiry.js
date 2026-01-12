// netlify/functions/inquiry.js
// Handles audit/work-with-us requests and adds to Notion database

const { Client } = require('@notionhq/client');

const notion = new Client({ auth: process.env.NOTION_API_KEY });
const databaseId = process.env.NOTION_INQUIRY_DB_ID;

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
      product_description,
      product_stage,
      engagement_type,
      source,
      details
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
        'Product Description': {
          rich_text: [{ text: { content: product_description || '' } }]
        },
        'Product Stage': {
          select: product_stage ? { name: product_stage } : null
        },
        'Engagement Type': {
          select: engagement_type ? { name: engagement_type } : null
        },
        Source: {
          select: source ? { name: source } : null
        },
        Details: {
          rich_text: [{ text: { content: details || '' } }]
        },
        Status: {
          select: { name: 'New' }
        },
        'Submitted At': {
          date: { start: new Date().toISOString() }
        }
      }
    });

    return {
      statusCode: 200,
      body: JSON.stringify({ success: true, message: 'Inquiry submitted successfully' })
    };

  } catch (error) {
    console.error('Inquiry submission error:', error);
    return {
      statusCode: 500,
      body: JSON.stringify({ error: 'Submission failed' })
    };
  }
};
