# Summary
- Standardized navigation and footer markup across pages with clean URL routing and no modal-based contact flows.
- Updated forms and Netlify function integrations to use Notion-backed endpoints with safe select handling.
- Cleaned interactive HTML to remove inline handlers (except mobile menu toggles) and removed Jotform embeds.

# Testing
- grep -R "jotform" -n .
- grep -R "openContactModal" -n .
- grep -R "onclick=" -n *.html
- grep -R "href=\"[^\"]*\.html" -n *.html

# Required Netlify environment variables
- NOTION_API_KEY
- NOTION_INQUIRY_DB_ID
- NOTION_ACCESS_DB_ID
- NOTION_NEWSLETTER_DB_ID

# Notion database schema notes
## Inquiry database (NOTION_INQUIRY_DB_ID)
- Name (title)
- Email (email)
- Organization (rich_text)
- Role (rich_text)
- Product Description (rich_text)
- Product Stage (select)
- Engagement Type (select)
- Source (select)
- Details (rich_text)
- Status (select)
- Submitted At (date)

## Access database (NOTION_ACCESS_DB_ID)
- Name (title)
- Email (email)
- Organization (rich_text)
- Role (rich_text)
- Intended Use (select)
- Description (rich_text)
- Status (select)
- Requested At (date)

## Newsletter database (NOTION_NEWSLETTER_DB_ID)
- Email (title)
- Subscribed At (date)
- Status (select)
- Source (select)
