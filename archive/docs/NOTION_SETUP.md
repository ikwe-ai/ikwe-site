# ikwe.ai Form → Notion Integration Setup

## Overview
The site has two forms that submit to Netlify serverless functions, which then write to Notion databases.

## Files Created
```
netlify/
├── functions/
│   ├── access-request.js   # Handles /request-access form
│   ├── inquiry.js          # Handles /inquiry form  
│   └── package.json        # Dependencies
└── netlify.toml            # Netlify configuration
```

---

## Step 1: Create Notion Integration

1. Go to https://www.notion.so/my-integrations
2. Click "New integration"
3. Name it "ikwe.ai Website"
4. Select your workspace
5. Click "Submit"
6. Copy the **Internal Integration Token** (starts with `secret_`)

---

## Step 2: Create Notion Databases

### Database 1: Access Requests
Create a database with these properties:

| Property Name | Type |
|--------------|------|
| Name | Title |
| Email | Email |
| Organization | Text |
| Role | Text |
| Intended Use | Select (options: Academic research, Product evaluation, Policy development, Journalism, Internal training, Other) |
| Description | Text |
| Status | Select (options: New, Reviewing, Approved, Denied) |
| Source | Select (options: Website Form) |
| Submitted | Date |

### Database 2: Engagement Inquiries
Create a database with these properties:

| Property Name | Type |
|--------------|------|
| Name | Title |
| Email | Email |
| Organization | Text |
| Role | Text |
| Product Description | Text |
| Product Stage | Select (options: Concept, Pre-launch, Live, Post-incident) |
| Engagement Type | Select (options: Snapshot, Audit, Advisory, Unsure) |
| Source | Select (options: Benchmark research, Policy requirement, Investor request, Internal concern, Incident, Referral, Other) |
| Details | Text |
| Status | Select (options: New, Contacted, In Progress, Closed) |
| Submitted | Date |

---

## Step 3: Share Databases with Integration

For EACH database:
1. Open the database page
2. Click "..." menu → "Add connections"
3. Select "ikwe.ai Website" integration
4. Click "Confirm"

---

## Step 4: Get Database IDs

For each database:
1. Open the database as a full page
2. Look at the URL: `https://notion.so/[workspace]/[DATABASE_ID]?v=...`
3. Copy the DATABASE_ID (32-character string)

---

## Step 5: Set Netlify Environment Variables

In Netlify dashboard → Site settings → Environment variables:

```
NOTION_API_KEY = secret_xxxxxxxxxxxxx
NOTION_ACCESS_REQUESTS_DB = xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
NOTION_INQUIRIES_DB = xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

---

## Step 6: Deploy

1. Push the `netlify/` folder to your repo
2. Netlify will auto-deploy the functions
3. Test by submitting each form

---

## Troubleshooting

**"Failed to submit"**
- Check Netlify function logs (Functions tab in dashboard)
- Verify environment variables are set
- Verify database is shared with integration

**"Property not found"**
- Make sure database property names match EXACTLY (case-sensitive)
- Make sure Select options exist in the database

---

## API Endpoints

Once deployed:
- `POST /api/access-request` → Creates Access Request
- `POST /api/inquiry` → Creates Engagement Inquiry

Both accept JSON body and return:
```json
{ "success": true, "id": "notion-page-id" }
```
