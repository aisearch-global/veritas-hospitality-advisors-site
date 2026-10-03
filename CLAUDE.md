# CLAUDE.md — Veritas Hospitality Advisors Site
*Session handoff file. Update after every working session.*
*Last updated: 3 October 2026 | Branch: main*

---

## Repo basics

| Item | Value |
|---|---|
| GitHub Pages URL | https://aisearch-global.github.io/veritas-hospitality-advisors-site/ |
| Production URL (target) | https://veritashospitalityadvisors.in |
| Active branch | `main` (content-fixes-oct26 merged and pushed) |
| Commits signed | Viv (viveka@aisearch.global) — never "Claude" |
| Push command | `git push origin main` |

---

## Design tokens

| Token | Value |
|---|---|
| `--ink` | `#1a3028` (dark green — nav bg, headings, body text on cream) |
| `--cream` | `#f5f4ef` (page background, logo text, light text on dark) |
| `--gold` | `#a57426` (accent — logo dot, CTA borders, highlights) |
| `--slate` | `rgba(26,48,40,.55)` (muted body text) |
| Body font | Public Sans (300/400/500/600) |
| Heading/logo font | Source Serif 4 (**weight 300, NOT italic** for logo — weight 300/400/600 for headings) |
| Nav height | 64px fixed |
| Logo font-size | **1.35rem** |
| Logo letter-spacing | `.04em` |
| Logo color | `var(--cream)` / `#f5f4ef` |
| Logo dot color | `var(--gold)` / `#a57426` |

### Logo exact CSS (copy verbatim to every page)
```css
.logo{font-family:"Source Serif 4",serif;font-weight:300;font-size:1.35rem;color:var(--cream);letter-spacing:.04em;text-decoration:none}
.logo span{color:var(--gold)}
```

### Logo SVG file
Saved at `img/veritas-logo.svg` — Source Serif 4 weight 300, cream text, gold dot, ink background.
Use for email headers, PDF exports, and any non-HTML context.

### Google Fonts URL (correct — loads all needed weights)
```html
<link href="https://fonts.googleapis.com/css2?family=Public+Sans:wght@300;400;500;600&family=Source+Serif+4:ital,wght@0,300;0,400;0,600;1,300&display=swap" rel="stylesheet">
```

### NEVER do this to the logo
- Do NOT set `font-style:italic` on `.logo`
- Do NOT set `font-weight:600` on `.logo`
- Do NOT set `font-size` other than `1.35rem`
- Do NOT change `letter-spacing` to negative values
- Do NOT use any font other than Source Serif 4 for the logo

---

## Nav pattern (ALL pages must match exactly)

```html
<nav>
  <a href="/" class="logo">Veritas<span>.</span></a>   <!-- ../ from perspectives/ -->
  <ul class="nav-links">
    <li><a href="/">Home</a></li>
    <li><a href="founder.html">Founder</a></li>
    <li><a href="clients.html">Clients</a></li>
    <li><a href="diagnostic.html">Diagnostic</a></li>
    <li><a href="insights.html">Perspectives</a></li>
    <li><a href="/#contact">Contact</a></li>
  </ul>
  <a href="mailto:vaishakh@veritashospitalityadvisors.com" class="nav-cta">Discuss confidentially</a>
</nav>
```
- Add `class="active"` to current page's link
- Logo href = `"/"` from root pages, `"../"` from `perspectives/` subfolder — **always links to homepage, every page including legal.html**
- Logo CSS must match exactly: Source Serif 4, weight 300, 1.35rem, letter-spacing .04em, NO italic
- Nav CTA: `mailto:vaishakh@veritashospitalityadvisors.com` — **never viveka@aisearch.global in public HTML**
- Display email rule: `vaishakh@veritashospitalityadvisors.com` everywhere public. `viveka@aisearch.global` is backend-only (git attribution, form service config that users cannot see)

---

## File map

```
/
├── index.html              Homepage — all viveka@ removed, hero bg-position center 65%
├── founder.html            Founder page — logo href /, nav links /, btn-email → Mail Vaishakh
├── clients.html            Clients page — logo href /, nav links / (all index.html refs removed)
├── diagnostic.html         Diagnostic wizard — logo href /, nav links /, JS mailto → vaishakh@
├── insights.html           Perspectives hub — logo 1.35rem, href /, Clients link added
├── legal.html              Privacy & Terms — logo 1.35rem, href /, 3 viveka@ removed
├── health-check.html       Internal — logo CSS fixed (weight 300, no italic, .04em spacing)
├── img/
│   ├── veritas-logo.svg                    NEW — SVG logo (Source Serif 4 wt300, cream, gold dot)
│   ├── vaishakh-suman-tarafdar.jpg         With Suman Tarafdar, Lyfe Bhubaneswar, Nov 2024
│   ├── vaishakh-naval-officers.jpg         With VAdm Saxena AVSM NM + RAdm Jha at Lyfe
│   ├── vaishakh-naval-officer-2.jpg        With senior naval officer at Lyfe
│   ├── obama-radisson-kuwait-team.jpg      Group photo at Radisson Blu Kuwait ~2008
│   ├── obama-radisson-signature.jpg        Autograph on Radisson SAS Kuwait letterhead
│   └── dhs-homeland-security-letter.jpg   DHS appreciation letter to Vaishakh
└── perspectives/
    ├── vaishakh-interview.html    Interview — nav + IGBC sustainability section updated
    ├── sustainability-hotel-india.html  Sustainability in Indian hotels article
    └── [10 existing industry analysis articles]
```

---

## Security constraints (permanent — read before every session)

**Never publish:**
- Vaishakh's date of birth, home/family addresses, UDID/disability number
- Old CV objective (targets GM/Cluster Head employment)
- Personal Gmail (vaishakh.surendran@gmail.com)
- Executive Profile PDF contents

**Never publish without Vaishakh's explicit confirmation:**
- **Obama claim**: CV says "Hosted President Barack Obama" at Radisson Blu Kuwait.
  Obama's confirmed Kuwait stop was July 2008 as senator/candidate.
  → Current wording is NEUTRAL: "managing US government delegations" — DO NOT name Obama until confirmed.
- **Employer naming**: Accor, Wyndham, ITC, Taj — get explicit consent before publishing brand names
- **GSTIN** (32BLFPS3361D1ZD) and **Udyam** (UDYAM-KL-07-0058097) — ask first
- **Mobility/disability** — only with explicit consent and Vaishakh's own framing

**Copy rules:**
- Never set the owner against his own team. Veritas works alongside GM and staff.
- Display email: vaishakh@veritashospitalityadvisors.com (visitor-facing — all public HTML)
- Backend/attribution: viveka@aisearch.global (git commits only — NEVER in rendered HTML)
- All viveka@ references have been removed from public HTML as of 3 Oct 2026

---

## Client: Sanskreti The Heritage

- First confirmed public advisory client (barter — case study + testimonial)
- Eco-island heritage resort, Kallanchery Island, North Kumbalanghi, Kochi, Kerala
- Vembanad backwaters; heritage rooms, grand villas, tree-house villa
- Restaurant: Thodu; Spa: Ahana (Ayurveda)
- Website: https://www.sanskretitheheritage.com/
- Named on clients.html and homepage — ownership confirmed naming OK
- **Pending**: LinkedIn copy from Vaishakh for client card body; property photo with consent

---

## Tab structure in insights.html

```javascript
switchTab('industry')  // panel id="panel-industry"
switchTab('essays')    // panel id="panel-essays"
switchTab('archive')   // panel id="panel-archive"
```
Article cards use class `art-card` (not `article-card` — different class).

---

## Pending tasks

- [ ] **Confirm Obama claim** with Vaishakh (date + title) — then can name him on carousel slide 4
- [ ] **Employer naming consent**: Accor, Wyndham, ITC, Taj
- [ ] **GSTIN/Udyam** publish consent
- [ ] **Sanskreti client page**: Vaishakh to provide LinkedIn copy + property photo with consent
- [ ] **robots.txt + sitemap.xml** (deferred)
- [ ] **Rebuild owner-playbook.pdf** (deferred)
- [ ] **Send signed service agreement** to Vaishakh (Viv action)
- [ ] **Send cold-run AEO findings** to Vaishakh (Viv action)
- [ ] **Delete stale remote branch**: `git push origin --delete agent-6abdb7d`
- [ ] **Resume PDF**: Build premium branded resume, add download button to founder.html
- [ ] **Presentation deck**: Build premium HTML artifact (artifact only, NOT added to site)
- [ ] **Update master reference artifact**: https://claude.ai/artifact/M8iJW4hjAsbWC8qhFVkXQt
- [x] ~~Revert display email viveka@ → vaishakh@ on go-live approval~~ — Done 3 Oct 2026: all viveka@ removed from public HTML; vaishakh@ wired throughout

---

## Commit history

| Commit | What |
|---|---|
| 5b6cba4 | insights.html: Archive tab YouTube only |
| 457b4bc | insights.html: Archive tab reel + full interview |
| cea6530 | vaishakh-interview.html + essay card + nav fixes |
| f2edbf4 | Clients page, carousel, sustainability article, Sanskreti homepage, IGBC, CLAUDE.md |
| (pending) | Full audit: logo CSS/href on all pages, all viveka@ removed, hero crop, SVG logo, CLAUDE.md |

---

*Maintained by AISearch Global (viveka@aisearch.global) on behalf of Veritas Hospitality Advisors.*
