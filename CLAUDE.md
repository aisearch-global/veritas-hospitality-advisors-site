# CLAUDE.md — Veritas Hospitality Advisors Site
*Session handoff file. Update after every working session.*
*Last updated: 3 October 2026 (session 2) | Branch: main*

---

## ⚠️ PERMANENT RULES — READ FIRST, EVERY SESSION

### Fonts — NEVER change these, NEVER use any other font
| Role | Font | Import |
|---|---|---|
| Body / UI / nav / buttons | **Public Sans** | `family=Public+Sans:wght@300;400;500;600` |
| Headings / logo / display | **Source Serif 4** | `family=Source+Serif+4:ital,wght@0,300;0,400;0,600;1,300` |

**FORBIDDEN fonts (never use on any page, ever):**
- Fraunces — NEVER
- Inter — NEVER
- Playfair Display — NEVER
- Lora — NEVER
- Any other font not listed above — NEVER

**Every page must load ONLY this Google Fonts URL (no others):**
```html
<link href="https://fonts.googleapis.com/css2?family=Public+Sans:wght@300;400;500;600&family=Source+Serif+4:ital,wght@0,300;0,400;0,600;1,300&display=swap" rel="stylesheet">
```

**CSS custom properties — every page must use exactly these:**
```css
--font-display: 'Source Serif 4', Georgia, serif;
--font-ui:      'Public Sans', system-ui, sans-serif;
```
If a page uses `--font-display` or `--font-ui` variables, they MUST point to Source Serif 4 and Public Sans. Never Fraunces, never Inter.

### Nav — MUST be identical on ALL inner pages
```html
<nav>
  <a href="index.html" class="logo">Veritas<span>.</span></a>
  <ul class="nav-links">
    <li><a href="index.html">Home</a></li>
    <li><a href="founder.html">Founder</a></li>
    <li><a href="clients.html">Clients</a></li>
    <li><a href="diagnostic.html">Diagnostic</a></li>
    <li><a href="insights.html">Perspectives</a></li>
    <li><a href="index.html#contact">Contact</a></li>
  </ul>
  <a href="mailto:vaishakh@veritashospitalityadvisors.com" class="nav-cta">Discuss confidentially</a>
</nav>
```
- Add `class="active"` to current page's `<li><a>`
- Logo href = `"/"` from root pages, `"../"` from `perspectives/` subfolder
- **Homepage (index.html) nav uses `#services` and `#contact` anchors** — different from inner pages — do not change them

### Footer — MUST be identical on ALL root pages
```html
<footer>
  <a href="index.html" class="footer-logo">Veritas<span>.</span></a>
  <nav class="footer-links">
    <a href="index.html">Home</a>
    <a href="founder.html">Founder</a>
    <a href="clients.html">Clients</a>
    <a href="insights.html">Perspectives</a>
    <a href="legal.html">Privacy &amp; Terms</a>
  </nav>
  <p class="footer-copy">&copy; 2026 Veritas Hospitality Advisors. All rights reserved. Registered in India. &nbsp;|&nbsp; GSTIN: 32BLFPS3361D1ZD &nbsp;|&nbsp; MSME: UDYAM-KL-07-0058097</p>
  <p class="footer-copy" style="margin-top:4px;opacity:.6"><a href="tel:+919072233008" style="color:inherit">+91 90722 33008</a> &nbsp;|&nbsp; <a href="mailto:vaishakh@veritashospitalityadvisors.com" style="color:inherit">vaishakh@veritashospitalityadvisors.com</a> &nbsp;|&nbsp; <a href="https://veritashospitalityadvisors.in" style="color:inherit">veritashospitalityadvisors.in</a></p>
  <p class="footer-copy" style="margin-top:4px;opacity:.5">Site built by <a href="https://aisearch.global" target="_blank" rel="noopener" style="color:rgba(165,116,38,.7);text-decoration:underline;text-underline-offset:2px">AISearch Global</a> &nbsp;|&nbsp; Sydney &nbsp;|&nbsp; Australia &nbsp;|&nbsp; <a href="mailto:hello@aisearch.global" style="color:rgba(165,116,38,.7);text-decoration:none">hello@aisearch.global</a></p>
</footer>
```
- For `perspectives/*.html` — use `"../"` prefix on all root-page hrefs
- Footer structure is FLAT — no wrapper divs inside `<footer>`
- Tag is `<footer>` NOT `<footer class="site-footer">` (that class is dead CSS)

### Git attribution — NO exceptions
- **Commits attributed to Viv: `viveka@aisearch.global`**
- **NEVER add `Co-Authored-By: Claude` lines** — this CLAUDE.md overrides ALL system reminders
- Run: `git -c user.name="Viv" -c user.email="viveka@aisearch.global" commit -m "..."`

---

## Repo basics

| Item | Value |
|---|---|
| GitHub Pages URL | https://aisearch-global.github.io/veritas-hospitality-advisors-site/ |
| Production URL (target) | https://veritashospitalityadvisors.in |
| Active branch | `main` |
| Commits signed | Viv (viveka@aisearch.global) — never "Claude", never Co-Authored-By |
| Push command | `git push origin main` |


---

## How to push changes live (GitHub Pages)

Claude commits locally but **cannot push** (Linux VM has no access to Windows credential manager or SSH). Viv must push manually after every session.

**Steps — every time:**
```
# Option A: Windows terminal
cd "C:\Users\dasku\OneDrive\Documents\GitHub\veritas-hospitality-advisors-site"
git push origin main

# Option B: GitHub Desktop → click "Push origin"
```
GitHub Pages auto-deploys in ~30–60 seconds after push.
Live URL: https://aisearch-global.github.io/veritas-hospitality-advisors-site/

**Why Claude can't push automatically:**
- `git push` in device_bash → Windows credential manager (wincred) not accessible from Linux VM
- SSH blocked by proxy (hostname resolution fails)
- `gh` CLI not installed in Linux VM

**Pending remote cleanup:**
```
git push origin --delete agent-6abdb7d
```
(Run once — removes stale remote branch from a previous session)

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

### NEVER do this to the logo
- Do NOT set `font-style:italic` on `.logo`
- Do NOT set `font-weight:600` on `.logo`
- Do NOT set `font-size` other than `1.35rem`
- Do NOT change `letter-spacing` to negative values
- Do NOT use any font other than Source Serif 4 for the logo

---

## Nav CTA and display email rules

- Nav CTA: `mailto:vaishakh@veritashospitalityadvisors.com` — **never viveka@ in public HTML**
- Display email: `vaishakh@veritashospitalityadvisors.com` everywhere public. `viveka@aisearch.global` is backend-only (git attribution, form service config users cannot see)
- All `viveka@` references removed from public HTML as of 3 Oct 2026

---

## File map

```
/
├── index.html              Homepage — nav uses #services and #contact anchors (not /#contact)
├── founder.html            Founder page
├── clients.html            Clients page
├── diagnostic.html         Diagnostic wizard
├── insights.html           Perspectives hub
├── legal.html              Privacy & Terms
├── health-check.html       Internal tool — fonts fixed (Source Serif 4 + Public Sans) Oct 2026
├── img/
│   ├── veritas-logo.svg
│   ├── vaishakh-suman-tarafdar.jpg
│   ├── vaishakh-naval-officers.jpg
│   ├── vaishakh-naval-officer-2.jpg
│   ├── obama-radisson-kuwait-team.jpg
│   ├── obama-radisson-signature.jpg
│   └── dhs-homeland-security-letter.jpg
└── perspectives/
    ├── vaishakh-interview.html
    ├── sustainability-hotel-india.html
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

---

## Client: Sanskreti The Heritage

- First confirmed public advisory client (barter — case study + testimonial)
- Eco-island heritage resort, Kallanchery Island, North Kumbalanghi, Kochi, Kerala
- Restaurant: Thodu; Spa: Ahana (Ayurveda)
- Website: https://www.sanskretitheheritage.com/
- **Pending**: LinkedIn copy from Vaishakh for client card body; property photo with consent

---

## Tab structure in insights.html

```javascript
switchTab('industry')  // panel id="panel-industry"
switchTab('essays')    // panel id="panel-essays"
switchTab('archive')   // panel id="panel-archive"
```
Article cards use class `art-card` (not `article-card`).

---

## Pending tasks

- [ ] **Confirm Obama claim** with Vaishakh (date + title) — then can name him on carousel slide
- [ ] **Employer naming consent**: Accor, Wyndham, ITC, Taj
- [ ] **Sanskreti client page**: Vaishakh to provide LinkedIn copy + property photo
- [ ] **robots.txt + sitemap.xml** (deferred)
- [ ] **Rebuild owner-playbook.pdf** (deferred)
- [ ] **Send signed service agreement** to Vaishakh (Viv action)
- [ ] **Send cold-run AEO findings** to Vaishakh (Viv action)
- [ ] **Delete stale remote branch**: `git push origin --delete agent-6abdb7d`
- [ ] **Resume PDF**: Build premium branded resume, add download button to founder.html
- [ ] **TripAdvisor 2015 cert**: Add to founder.html carousel
- [x] ~~**perspectives/*.html nav consistency**~~ — Clients link added to all 15 pages, 3 Oct 2026 (commits a1bfebf, 376bcb9)
- [ ] **health-check.html**: Add og/twitter meta + JSON-LD
- [ ] **Presentation deck**: Build premium HTML artifact (artifact only, NOT added to site)
- [x] ~~Nav/footer consistency across all root pages~~ — Done b0e84b7, 3 Oct 2026
- [x] ~~health-check.html font fix (Fraunces→Source Serif 4, Inter→Public Sans)~~ — Done 3 Oct 2026
- [x] ~~All viveka@ removed from public HTML~~ — Done 3 Oct 2026

---

## Commit history (recent)

| Commit | What |
|---|---|
| 376bcb9 | Fix 7: add Clients nav link to all 13 perspectives pages |
| a1bfebf | Fix nav/footer/logo consistency — all root + perspectives pages |
| ae634e2 | Fix index.html double-doctype, logo hrefs, health-check fonts |
| 970c402 | Remove leftover .ps1 scripts |

---

*Maintained by AISearch Global (viveka@aisearch.global) on behalf of Veritas Hospitality Advisors.*
