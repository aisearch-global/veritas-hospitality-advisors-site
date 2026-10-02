# CLAUDE.md — Veritas Hospitality Advisors Site
*Session handoff file. Keep updated after every working session.*
*Last updated: 2 October 2026 | Branch: content-fixes-oct26*

---

## Repo basics

| Item | Value |
|---|---|
| GitHub Pages URL | https://aisearch-global.github.io/veritas-hospitality-advisors-site/ |
| Production URL (target) | https://veritashospitalityadvisors.in |
| Active branch | `content-fixes-oct26` |
| Commits signed | Viv (viveka@aisearch.global) — never "Claude" |
| Push command | `git push origin content-fixes-oct26` |

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

---

## File map

```
/
├── index.html              Homepage — updated Oct 2: Clients in nav, Sanskreti section added
├── founder.html            Founder page — updated Oct 2: Clients in nav, photo carousel added
├── clients.html            NEW Oct 2 — Clients page with Sanskreti The Heritage card
├── diagnostic.html         Free diagnostic / lead capture
├── insights.html           Perspectives hub — updated Oct 2: Clients in nav, sustainability card
├── legal.html              Privacy & Terms
├── img/                    NEW Oct 2 — photos committed to repo
│   ├── vaishakh-suman-tarafdar.jpg         With Suman Tarafdar at Lyfe Bhubaneswar, Nov 2024
│   ├── vaishakh-naval-officers.jpg         With VAdm Saxena AVSM NM + RAdm Jha at Lyfe
│   ├── vaishakh-naval-officer-2.jpg        With senior naval officer at Lyfe
│   ├── obama-radisson-kuwait-team.jpg      Group photo at Radisson Blu Kuwait, ~2008
│   ├── obama-radisson-signature.jpg        Autograph on Radisson SAS Kuwait letterhead
│   └── dhs-homeland-security-letter.jpg   DHS appreciation letter to Vaishakh
└── perspectives/
    ├── vaishakh-interview.html    Interview — updated Oct 2: Clients in nav, IGBC passage added
    ├── sustainability-hotel-india.html  NEW Oct 2 — sustainability article
    └── [10 existing industry analysis articles]
```

---

## Security constraints (permanent)

**Never publish:**
- Vaishakh's date of birth, home/family addresses, UDID/disability number
- Old CV objective (targets GM/Cluster Head employment — pre-dates VHA)
- Personal Gmail (vaishakh.surendran@gmail.com)
- Executive Profile PDF contents

**Never publish without Vaishakh's explicit confirmation:**
- Obama claim: CV says "Hosted President Barack Obama" at Radisson Blu Kuwait.  
  Obama's confirmed Kuwait stop was July 2008 as senator/candidate — confirm date and title.  
  → Current site wording is NEUTRAL: "managing US government delegations" — do not name Obama.
- Accor, Wyndham, ITC, Taj: get explicit employer-naming consent before publishing brand names.
- GSTIN (32BLFPS3361D1ZD) and Udyam (UDYAM-KL-07-0058097): ask before publishing.
- Mobility/disability: only with explicit consent and Vaishakh's own framing.

**Copy rules:**
- Never set the owner against his own team. Veritas works alongside GM and staff.
- Display email always: vaishakh@veritashospitalityadvisors.com
- Backend/attribution: viveka@aisearch.global (AISearch Global built the site)
- Revert viveka@ → vaishakh@ display references only on go-live approval

---

## Nav pattern (all pages must match)

```html
<ul class="nav-links">
  <li><a href="/">Home</a></li>           <!-- or "../" from perspectives/ -->
  <li><a href="founder.html">Founder</a></li>
  <li><a href="clients.html">Clients</a></li>
  <li><a href="diagnostic.html">Diagnostic</a></li>
  <li><a href="insights.html">Perspectives</a></li>
  <li><a href="/#contact">Contact</a></li>
</ul>
```
Add `class="active"` to the current page's link.

---

## Client: Sanskreti The Heritage

- **First confirmed public advisory client** (barter engagement — case study + testimonial)
- Eco-island heritage resort, Kallanchery Island, North Kumbalanghi, Kochi, Kerala
- Vembanad backwaters; luxury heritage rooms, grand villas, tree-house villa
- Restaurant: Thodu (Kerala cuisine); Spa: Ahana (Ayurveda)
- Website: https://www.sanskretitheheritage.com/
- Named on clients.html and homepage (Sanskreti confirmed naming)
- **Pending from Vaishakh:** explicit LinkedIn/copy consent for any specific claims

---

## Pending tasks

- [ ] **Push branch**: `git push origin content-fixes-oct26`
- [ ] **PR/merge** content-fixes-oct26 into main for deployment
- [ ] **Confirm Obama claim** with Vaishakh (date, title) before naming him
- [ ] **Employer naming consent**: Accor, Wyndham, ITC, Taj
- [ ] **GSTIN/Udyam** publish consent
- [ ] **Sanskreti LinkedIn copy**: Vaishakh to provide LinkedIn copy for client page
- [ ] **Sanskreti property image**: add image with owner consent
- [ ] **robots.txt + sitemap.xml** (deferred)
- [ ] **Rebuild owner-playbook.pdf** (deferred)
- [ ] **Send signed service agreement** to Vaishakh (Viv action)
- [ ] **Send cold-run AEO findings** to Vaishakh (Viv action)
- [ ] **Delete stale remote branch**: `git push origin --delete agent-6abdb7d`
- [ ] **Revert** backend viveka@ references to vaishakh@ on go-live approval

---

## Commit history (branch content-fixes-oct26)

| Hash | What |
|---|---|
| (initial) | Branch created from main |
| cea6530 | vaishakh-interview.html + insights.html cards + nav fixes |
| (pending) | clients.html + sustainability article + founder carousel + Sanskreti homepage + IGBC interview update + CLAUDE.md |

---

## Tab structure in insights.html

```javascript
switchTab('industry')  // Industry Analysis panel: id="panel-industry"
switchTab('essays')    // Owner Essays panel:     id="panel-essays"
switchTab('archive')   // Archive panel:          id="panel-archive"
```

---

*Maintained by AISearch Global (viveka@aisearch.global) on behalf of Veritas Hospitality Advisors.*
