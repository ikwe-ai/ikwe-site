# IKWE.AI - Clean Site Package

**Generated:** January 11, 2026  
**Purpose:** Complete, deployment-ready site with all fixes applied

---

## 📁 File Manifest

### HTML Pages (11 files) — REQUIRED
| File | Path | Purpose |
|------|------|---------|
| `index.html` | `/` | Homepage |
| `emotional-safety-gap.html` | `/emotional-safety-gap` | Key findings |
| `research.html` | `/research` | Methodology |
| `about.html` | `/about` | About page |
| `press.html` | `/press` | Press kit |
| `inquiry.html` | `/inquiry` | Contact form (Notion-integrated) |
| `explorer.html` | `/explorer` | Scenario explorer |
| `faq.html` | `/faq` | FAQ |
| `blog.html` | `/blog` | Research updates |
| `privacy.html` | `/privacy` | Privacy policy |
| `terms.html` | `/terms` | Terms of service |

### Config Files (4 files) — REQUIRED
| File | Purpose |
|------|---------|
| `_redirects` | Netlify redirect rules (clean URLs + API routes) |
| `netlify.toml` | Netlify build config + headers |
| `sitemap.xml` | Search engine sitemap |
| `robots.txt` | Search engine directives |

### Netlify Functions (3 files) — REQUIRED for forms
| File | Endpoint | Purpose |
|------|----------|---------|
| `netlify/functions/newsletter.js` | `/api/newsletter` | Blog newsletter signup |
| `netlify/functions/inquiry.js` | `/api/inquiry` | Audit/work requests |
| `netlify/functions/access-request.js` | `/api/access-request` | Research access requests |

### Assets — COPY FROM EXISTING REPO
These files should be copied from your existing repo (not regenerated):
- `ikwe_logo_dark.png` — Site logo
- `ikwe_logo_light.png` — Light version
- `ikwe-press-og.png` — Press OG image
- `og/` folder — OG images for each page
- `styles.css` — If using external CSS (most styles are inline)

---

## ✅ All Fixes Applied

| Issue | Status |
|-------|--------|
| Desktop nav missing FAQ/Blog | ✅ Fixed |
| Internal links with `.html` | ✅ Removed (all use `/page`) |
| onclick modal handlers | ✅ Converted to `/inquiry` links |
| Footer inconsistencies | ✅ Standardized 4-column layout |
| Form dependencies | ✅ Replaced with Notion API |
| Clean URL routing | ✅ `_redirects` configured |
| Canonical/OG URLs | ✅ All use clean paths |

---

## 🚀 Deployment Instructions

### Step 1: Prepare Notion Databases

Create 3 databases in Notion:

**Newsletter Database:**
- Email (Title)
- Subscribed At (Date)
- Status (Select: Active, Unsubscribed)
- Source (Select: Blog, Other)

**Inquiry Database:**
- Name (Title)
- Email (Email)
- Organization (Text)
- Role (Text)
- Product Description (Text)
- Product Stage (Select)
- Engagement Type (Select)
- Source (Select)
- Details (Text)
- Status (Select: New, Contacted, Closed)
- Submitted At (Date)

**Access Request Database:**
- Name (Title)
- Email (Email)
- Organization (Text)
- Role (Text)
- Intended Use (Select)
- Description (Text)
- Status (Select: Pending, Approved, Denied)
- Requested At (Date)

### Step 2: Get Notion Integration

1. Go to https://www.notion.so/my-integrations
2. Create new integration for "Ikwe Forms"
3. Copy the API key
4. Share each database with the integration

### Step 3: Configure Netlify Environment Variables

In Netlify Dashboard → Site settings → Environment variables:

```
NOTION_API_KEY=secret_xxxxxxxxxxxxx
NOTION_NEWSLETTER_DB_ID=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
NOTION_INQUIRY_DB_ID=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
NOTION_ACCESS_DB_ID=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

### Step 4: Install Dependencies

Create `package.json` in root:
```json
{
  "name": "ikwe-site",
  "dependencies": {
    "@notionhq/client": "^2.2.0"
  }
}
```

### Step 5: Deploy

1. Replace all files in your `ikwe-site` repo with this package
2. Add your existing assets (logos, OG images)
3. Commit and push
4. Netlify will auto-deploy

### Step 6: Verify

Test these URLs:
- `https://ikwe.ai/emotional-safety-gap.html` → should 301 redirect
- `https://ikwe.ai/emotional-safety-gap` → should show page
- `https://ikwe.ai/inquiry` → should show form
- Submit test form → should appear in Notion

---

## 🔗 URL Structure

| Clean URL | Serves | Redirect From |
|-----------|--------|---------------|
| `/` | `index.html` | `/index.html` |
| `/emotional-safety-gap` | `emotional-safety-gap.html` | `/emotional-safety-gap.html`, `/gap`, `/findings` |
| `/research` | `research.html` | `/research.html`, `/methodology` |
| `/about` | `about.html` | `/about.html` |
| `/press` | `press.html` | `/press.html`, `/media` |
| `/inquiry` | `inquiry.html` | `/inquiry.html`, `/contact`, `/request-access` |
| `/explorer` | `explorer.html` | `/explorer.html` |
| `/faq` | `faq.html` | `/faq.html`, `/questions` |
| `/blog` | `blog.html` | `/blog.html`, `/updates`, `/news` |
| `/privacy` | `privacy.html` | `/privacy.html` |
| `/terms` | `terms.html` | `/terms.html` |

---

## 📧 Contact

All forms submit to: `research@ikwe.ai` (via Notion)
