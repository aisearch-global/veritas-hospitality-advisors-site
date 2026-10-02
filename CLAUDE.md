# CLAUDE.md — Veritas Hospitality Advisors Site
*Session handoff file. Update after every working session.*
*Last updated: 2 October 2026 | Branch: main (merged from content-fixes-oct26)*

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
| `--ink` | `#1a3028` (dark green) |
| `--cream` | `#f5f4ef` |
| `--gold` | `#a57426` |
| `--slate` | `rgba(26,48,40,.55)` |
| Body font | Public Sans (300/400/500/600) |
| Heading/logo font | Source Serif 4 (italic, 300/400/600) |
| Nav height | 64px fixed |
| Logo font-size | **1.35rem** (bumped from 1.1rem on 2 Oct) |

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
- Logo href = `"/"` from root pages, `"../"` from `perspectives/` subfolder
- Logo font-size in local `<style>`: `font-size:1.35rem`
- Logo must link to homepage on every page — confirmed working

---

## File map

```
/
├── index.html              Homepage — nav updated, Sanskreti Current Engagement section
├── founder.html            Founder page — nav updated, photo carousel (4 slides)
├── clients.html            NEW — Clients page with Sanskreti The Heritage
├── diagnostic.html         Diagnostic wizard — nav updated (Clients added Oct 2)
├── insights.html           Perspectives hub — nav updated, sustainability card added
├── legal.html              Privacy & Terms
├── img/                    NEW — photos
│   ├── vaishakh-suman-tarafdar.jpg         With Suman Tarafdar, Lyfe Bhubaneswar, Nov 2024
│   ├── vaishakh-naval-officers.jpg         With VAdm Saxena AVSM NM + RAdm Jha at Lyfe
│   ├── vaishakh-naval-officer-2.jpg        With senior naval officer at Lyfe
│   ├── obama-radisson-kuwait-team.jpg      Group photo at Radisson Blu Kuwait ~2008
│   ├── obama-radisson-signature.jpg        Autograph on Radisson SAS Kuwait letterhead
│   └── dhs-homeland-security-letter.jpg   DHS appreciation letter to Vaishakh
└── perspectives/
    ├── vaishakh-interview.html    Interview — nav + IGBC sustainability section updated
    ├── sustainability-hotel-india.html  NEW — sustainability in Indian hotels article
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
- Display email: vaishakh@veritashospitalityadvisors.com (visitor-facing)
- Backend/attribution: viveka@aisearch.global (AISearch Global built the site)
- Revert viveka@ display references to vaishakh@ on go-live approval only

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
- [ ] **Revert** display email viveka@ → vaishakh@ on go-live approval

---

## Commit history

| Commit | What |
|---|---|
| 5b6cba4 | insights.html: Archive tab YouTube only |
| 457b4bc | insights.html: Archive tab reel + full interview |
| cea6530 | vaishakh-interview.html + essay card + nav fixes |
| f2edbf4 | Clients page, carousel, sustainability article, Sanskreti homepage, IGBC, CLAUDE.md |
| (pending) | Logo size 1.35rem, Clients in diagnostic nav, logo homepage link verified |

---

*Maintained by AISearch Global (viveka@aisearch.global) on behalf of Veritas Hospitality Advisors.*
