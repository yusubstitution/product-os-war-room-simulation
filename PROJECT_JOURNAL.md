# Product OS War Room Simulation - Project Journal

## Project Overview
**Owner:** Jason Yu
**Purpose:** Create a simulation game for 20 TPMs at R&D Offsite to demonstrate that "Manual Signal Processing" fails at scale
**Key Insight:** TPMs will be distracted by "Noise" (loud customers, urgent requests) and miss "Signal" (boring data with high ARR potential)

## Simulation Design

### Game Mechanics
- **Teams:** Groups of 3 (Sales Lead + Engineering Lead + TPM)
- **Constraint:** 100 story points budget
- **Goal:** Select top 5 features that maximize ARR potential
- **Challenge:** Each role gets different, disconnected data sources that must be manually reconciled

### The "Gotcha"
Some features will appear critical (loud customers, executive escalations) but have low actual ARR impact. Meanwhile, boring features buried in data will have high ARR potential but be easy to overlook.

---

## Artifacts Needed

### 1. Company & Product Setup
- [ ] **Company Overview Document** - Fictional B2B SaaS company background
- [ ] **Legacy Product Profile** - Enterprise-focused product details
- [ ] **Growth Product Profile** - SMB-focused product details

### 2. Feature Backlog (The "Answer Key")
- [ ] **Master Feature List** - All candidate features with:
  - Feature ID, Name, Description
  - Story Points (effort)
  - **TRUE ARR Potential** (hidden from players)
  - **Noise Level** (how loud/urgent it appears)
  - Signal vs Noise classification
- [ ] **Optimal Solution** - The actual best 5 features (for debrief)

### 3. Role-Specific Information Packets
- [ ] **Sales Lead Packet** - Customer conversations, escalations, deal blockers
- [ ] **Engineering Lead Packet** - Technical debt, architecture constraints, implementation complexity
- [ ] **TPM Packet** - Usage analytics, support tickets, partial ARR data

### 4. Simulation Materials
- [ ] **Facilitator Guide** - How to run the simulation, timing, debrief talking points
- [ ] **Team Worksheet** - Template for teams to fill out their selected features
- [ ] **Scoring Rubric** - How to calculate each team's total ARR vs optimal solution

### 5. Synthetic Data Sources (The Messy Data)
- [ ] **Sales CRM Export** - Deal notes, customer quotes, urgency flags
- [ ] **Support Ticket Summary** - Volume by feature request, sentiment
- [ ] **Product Analytics Dashboard** - Usage metrics, adoption rates
- [ ] **Executive Email Thread** - Escalations and "strategic priorities"

---

## Build Status

**Current Phase:** Planning & Company Design
**Started:** 2026-02-17

### Session Log

#### 2026-02-17: Project Kickoff & Feature Design
- Created project structure
- Defined simulation mechanics and objectives
- Outlined artifact list
- ✅ Designed EventFlow company profile (event management platform)
- ✅ Created master features list with 14 features:
  - 3 Traps (high noise, low signal)
  - 3 Hidden Gems (low noise, high signal)
  - 5 Defensible (Engineering's original 100pt roadmap)
  - 3 Bad Ideas (obvious duds)
- ✅ Defined optimal solution: 98pts, ~$16.1M ARR vs likely selection: ~$3.4M ARR (21% of optimal!)
- ✅ Built Engineering Lead packet - Complete feature catalog with descriptions, story points, complexity notes
- ✅ Built Sales Lead packet - 3 customer call transcripts (6 pages) + 3 escalation emails
  - Transcripts have loud trap demands but buried hidden gem hints
  - MegaCorp, TechConf, InnovateCorp scenarios

**TPM Packet Decision: Streamlit Dashboard**
- Building interactive analytics dashboard instead of static markdown
- Will host on Streamlit Community Cloud (Jason has account)
- Dashboard tabs:
  - Tab 1: Overview (vanity metrics)
  - Tab 2: Registration Funnel Analysis (F04 mobile signal)
  - Tab 3: Support Ticket Analysis (F05 cloning signal)
  - Tab 4: Feature Usage & Retention (F06 analytics correlation - THE GOLDEN DATA)
  - Tab 5: Customer Segment Breakdown
- Generate synthetic CSVs to feed the dashboard
- Signal is buried across different tabs (time pressure forces prioritization)

**Completed:**
1. ✅ Designed fictional company (EventFlow - event management platform)
2. ✅ Created master feature backlog (14 features with answer key)
3. ✅ Generated Engineering Lead packet (8-page feature catalog)
4. ✅ Generated Sales Lead packet (9 pages: 3 transcripts + 3 escalation emails)
5. ✅ Built TPM Streamlit dashboard + synthetic data
   - Set up Python virtual environment
   - Installed dependencies (streamlit, pandas, plotly, numpy)
   - Generated synthetic CSVs (4 files with embedded signals)
   - Built 5-tab interactive dashboard (app.py)
   - Tested locally - verified all tabs working
6. ✅ Created deployment documentation
   - README.md with full project overview
   - DEPLOYMENT_CHECKLIST.md for Streamlit Cloud deployment
   - TPM packet instructions (tpm-packet-instructions.md)

---

## WHERE WE ARE (End of Session - 2026-02-17)

**Status:** All core materials built and tested locally. Ready for deployment.

**What's Complete:**
- ✅ Company profile (EventFlow - event management SaaS)
- ✅ Master features list (14 features with answer key - DO NOT SHARE)
- ✅ Engineering Lead packet (8 pages - feature catalog)
- ✅ Sales Lead packet (9 pages - transcripts + escalations)
- ✅ TPM Streamlit dashboard (5 tabs with buried signals)
- ✅ Synthetic data (4 CSV files)
- ✅ Local testing (dashboard works perfectly)
- ✅ Deployment documentation (README, checklist, TPM instructions)

**Completed (2026-02-18):**
1. ✅ Deployed dashboard to Streamlit Cloud
   - URL: https://appuct-os-war-room-simulation-gzuxkhqjlfrfmbh5nhfhsy.streamlit.app/
   - Fixed duplicate chart key errors
   - Pushed to GitHub: https://github.com/yusubstitution/product-os-war-room-simulation
   - Updated TPM instructions with live URL
2. ✅ Created facilitator guide (23 pages)
   - Pre-simulation checklist
   - Detailed run-of-show with timing
   - Debrief script with talking points
   - Troubleshooting and tips
3. ✅ Created team worksheet template
   - Simple 1-page form for recording selections
4. ✅ Created scoring rubric (CSV)
   - All 14 features with true ARR values
   - Optimal solution reference
   - Team scoring calculator
   - Trap/gem tracking

**What's Left:**
1. Print materials for offsite (Jason to do before session)
   - 6-7 copies of each role packet
   - 6-7 team worksheets
   - Facilitator guide
2. Convert docs to Google Docs (optional, Jason to do)
3. Arrange laptops/tablets for TPMs

---

## NEXT STEPS (Resume Tomorrow)

### 1. Deploy to Streamlit Cloud (30 minutes)

**Follow DEPLOYMENT_CHECKLIST.md:**

```bash
# Step 1: Test locally one more time
cd /Users/jyu/Documents/20\ -\ Claude\ Code\ Projects/product-os-war-room-simulation
source venv/bin/activate
streamlit run app.py
# Visit http://localhost:8501 and verify all 5 tabs work

# Step 2: Initialize git (if not done)
git init
git add app.py generate_data.py requirements.txt data/*.csv
git add role-packets/*.md company-profile.md README.md .gitignore
git add DEPLOYMENT_CHECKLIST.md
git commit -m "Add Product OS War Room simulation dashboard"

# Step 3: Create GitHub repo
# - Go to https://github.com/new
# - Name: product-os-war-room-simulation
# - Public repo is fine (fake data)
# - Don't initialize with README

# Step 4: Push to GitHub
git remote add origin https://github.com/YOUR_USERNAME/product-os-war-room-simulation.git
git branch -M main
git push -u origin main

# Step 5: Deploy on Streamlit Cloud
# - Go to https://share.streamlit.io/
# - Sign in with GitHub
# - Click "New app"
# - Repository: YOUR_USERNAME/product-os-war-room-simulation
# - Branch: main
# - Main file path: app.py
# - Click "Deploy!"

# Step 6: Test deployed URL
# - Wait 2-3 minutes for deployment
# - Test all 5 tabs in the deployed app
# - Copy the URL (something like: https://your-app.streamlit.app)

# Step 7: Update TPM instructions
# - Edit role-packets/tpm-packet-instructions.md
# - Replace "[DASHBOARD URL WILL BE PROVIDED]" with actual URL
# - Commit and push update to GitHub
```

### 2. Create Facilitator Guide (30 minutes)

**File:** `facilitator-guide.md`

**Contents:**
- Pre-simulation setup (room setup, materials check)
- Run-of-show with timing
  - 5 min: Intro and team assignment
  - 10 min: Individual review
  - 20 min: Team discussion
  - 5 min: Submit selections
- Debrief script
  - Reveal true ARR impact of each feature
  - Show optimal solution (F04 + F05 + F06 + 2 defensible = $16M)
  - Compare to team selections (likely ~$3.4M = 21% of optimal)
  - Key talking points:
    - Why did teams pick traps? (loud noise, urgent escalations)
    - Where was the signal hidden? (boring data, page 4, tab 3)
    - Why manual signal processing fails at scale
    - How Product Ops SENSE pillar solves this (VoC dashboards, automated tagging)
- Handling questions

### 3. Create Team Worksheet (15 minutes)

**File:** `team-worksheet.md` or Google Doc

**Template:**
```
PRODUCT OS WAR ROOM - TEAM WORKSHEET

Team Name: _________________
Team Members:
- Engineering Lead: _________________
- Sales Lead: _________________
- TPM: _________________

GOAL: Select 5 features that maximize ARR within 100 story points

YOUR SELECTIONS:
┌────────────────────────────────────────────────────────┐
│ Feature ID | Feature Name           | Story Points    │
├────────────────────────────────────────────────────────┤
│ F__        | _____________________  | ___            │
│ F__        | _____________________  | ___            │
│ F__        | _____________________  | ___            │
│ F__        | _____________________  | ___            │
│ F__        | _____________________  | ___            │
├────────────────────────────────────────────────────────┤
│ TOTAL:     |                        | ___ / 100      │
└────────────────────────────────────────────────────────┘

WHY DID YOU CHOOSE THESE?
(2-3 sentences on your prioritization rationale)
___________________________________________________________
___________________________________________________________
___________________________________________________________

TOUGHEST TRADE-OFFS:
(What did you almost pick but cut? Why?)
___________________________________________________________
___________________________________________________________
```

### 4. Create Scoring Rubric (15 minutes)

**File:** `scoring-rubric.md` or spreadsheet

**Contents:**
- Master list of all 14 features with true ARR impact
- Formula to calculate team's total ARR
- Comparison to optimal solution ($16.1M)
- Percentage score (Team ARR / Optimal ARR)
- Breakdown showing which traps teams fell for
- Visual for debrief (bar chart comparing teams)

### 5. Additional Enhancements (Optional)

If time permits before offsite:

**A. Add "hints" mode to dashboard**
- Hidden button that reveals which metrics are most important
- For facilitator use during debrief

**B. Create debrief slides**
- Slide 1: All team selections
- Slide 2: ARR impact comparison
- Slide 3: Optimal solution revealed
- Slide 4: "Where was the signal?" (screenshots from dashboard)
- Slide 5: "Why manual processing fails"
- Slide 6: "The SENSE pillar solution"

**C. Add "competitive analysis" tab to dashboard**
- Show MegaCorp and TechConf as single data points
- Contrast with broader patterns
- Makes the trap even more obvious in hindsight

---

## FILES TO KEEP PRIVATE (Do Not Commit to Public GitHub)

- `master-features-list.md` - Contains answer key
- Facilitator guide debrief section (has answers)
- Scoring rubric (has true ARR values)

If making GitHub repo public, either:
- Keep these files local only
- Create a private `solutions/` folder in .gitignore
- Or make the entire repo private

---

## RESOURCES FOR TOMORROW

**Key Files:**
- `DEPLOYMENT_CHECKLIST.md` - Step-by-step Streamlit deployment
- `README.md` - Full project overview
- `master-features-list.md` - Answer key with all ARR values

**Test Command:**
```bash
cd /Users/jyu/Documents/20\ -\ Claude\ Code\ Projects/product-os-war-room-simulation
source venv/bin/activate
streamlit run app.py
```

**When Ready to Resume:** Tell Claude "continue with Product OS War Room" and reference this journal.

---

## Design Principles

1. **Realistic Noise** - The "loud" features should feel genuinely urgent (exec escalations, big logos, competitive pressure)
2. **Hidden Signal** - High-value features should be buried in boring metrics (usage trends, retention data, support efficiency gains)
3. **Information Asymmetry** - Each role sees only part of the picture; coordination is required but difficult
4. **Time Pressure** - TPMs will have limited time to reconcile data, forcing gut decisions
5. **Debrief Impact** - The reveal should clearly show how manual processes fail at scale

---

## Success Criteria

- [ ] 6-7 teams participate (20 TPMs ÷ 3 per team)
- [ ] Most teams select suboptimal roadmap (proving the point)
- [ ] At least 2-3 "trap" features are commonly selected (high noise, low signal)
- [ ] Debrief clearly demonstrates need for automated signal processing tools
