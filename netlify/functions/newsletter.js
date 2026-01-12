// netlify/functions/newsletter.js
// Adds newsletter subscribers to Notion database

const { Client } = require('@notionhq/client');

const notion = new Client({ auth: process.env.NOTION_API_KEY });
const databaseId = process.env.NOTION_NEWSLETTER_DB_ID;

exports.handler = async (event) => {
  // Only allow POST
  if (event.httpMethod !== 'POST') {
    return {
      statusCode: 405,
      body: JSON.stringify({ error: 'Method not allowed' })
    };
  }

  try {
    const { email } = JSON.parse(event.body);
    
    if (!email || !email.includes('@')) {
      return {
        statusCode: 400,
        body: JSON.stringify({ error: 'Valid email required' })
      };
    }

    // Add to Notion database
    await notion.pages.create({
      parent: { database_id: databaseId },
      properties: {
        Email: {
          title: [{ text: { content: email } }]
        },
        'Subscribed At': {
          date: { start: new Date().toISOString() }
        },
        Status: {
          select: { name: 'Active' }
        },
        Source: {
          select: { name: 'Blog' }
        }
      }
    });

    return {
      statusCode: 200,
      body: JSON.stringify({ success: true, message: 'Subscribed successfully' })
    };

  } catch (error) {
    console.error('Newsletter subscription error:', error);
    return {
      statusCode: 500,
      body: JSON.stringify({ error: 'Subscription failed' })
    };
  }
};
