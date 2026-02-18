# Product OS War Room Simulation

A hands-on simulation for TPMs to demonstrate that "Manual Signal Processing" fails at scale.

## Overview

Teams of 3 (Sales Lead + Engineering Lead + TPM) must build an optimal product roadmap from disconnected, messy data sources. They will likely miss the optimal solution because they'll be distracted by "Noise" (loud customers) and miss the "Signal" (boring data).

**Simulation Goal:** Select top 5 features within 100 story points that maximize ARR potential.

---

## Project Structure

```
product-os-war-room-simulation/
├── company-profile.md           # EventFlow company background
├── master-features-list.md      # ANSWER KEY - Do not share with participants
├── role-packets/
│   ├── engineering-lead-packet.md   # Feature catalog (shared reference)
│   ├── sales-lead-packet.md         # Customer transcripts + escalations (the NOISE)
│   └── (TPM packet is the Streamlit dashboard)
├── data/                        # Synthetic CSV data for dashboard
│   ├── registration_funnel.csv
│   ├── support_tickets.csv
│   ├── feature_usage_retention.csv
│   └── customer_segments.csv
├── app.py                       # TPM Streamlit dashboard (the SIGNAL)
├── generate_data.py             # Script to regenerate synthetic data
├── requirements.txt             # Python dependencies
└── venv/                        # Virtual environment (not committed to git)
```

---

## The Three Hidden Gems (Buried in TPM Dashboard)

**F04: Mobile Registration Optimization** (20 pts, $5M impact)
- Signal buried in Tab 2: "Registration Funnel Analysis"
- 62% mobile traffic, 51% abandonment vs 28% desktop
- 18,000 lost registrations/month

**F05: Event Cloning & Templates** (18 pts, $3.5M impact)
- Signal buried in Tab 3: "Support Tickets"
- 247 Q4 tickets requesting this feature (2nd highest category)

**F06: Advanced Analytics Dashboard** (25 pts, $6M impact)
- Signal buried in Tab 4: "Feature Usage & Retention"
- 95% retention for analytics users vs 73% for non-users
- Only 31% currently use analytics (huge opportunity)

**Optimal Solution: F04 + F05 + F06 + two defensible features = ~$16M ARR (98 points)**

---

## Local Development & Testing

### Setup (First Time)

```bash
# Navigate to project folder
cd product-os-war-room-simulation

# Create virtual environment (if not exists)
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate  # Mac/Linux
# or
venv\Scripts\activate     # Windows

# Install dependencies
pip install -r requirements.txt
```

### Run Dashboard Locally

```bash
# Activate virtual environment
source venv/bin/activate

# Run Streamlit app
streamlit run app.py

# Dashboard opens at http://localhost:8501
```

### Regenerate Synthetic Data (Optional)

```bash
source venv/bin/activate
python generate_data.py
```

---

## Deploying to Streamlit Cloud

### Prerequisites
- GitHub account (or other git provider)
- Streamlit Community Cloud account (free at https://streamlit.io/cloud)

### Deployment Steps

1. **Initialize Git Repository (if not done)**
   ```bash
   cd product-os-war-room-simulation
   git init
   git add .
   git commit -m "Initial commit: Product OS War Room simulation"
   ```

2. **Push to GitHub**
   ```bash
   # Create a new repository on GitHub (e.g., "product-os-war-room-simulation")
   # Then push your local repo:
   git remote add origin https://github.com/YOUR_USERNAME/product-os-war-room-simulation.git
   git branch -M main
   git push -u origin main
   ```

3. **Deploy on Streamlit Cloud**
   - Go to https://streamlit.io/cloud
   - Sign in with GitHub
   - Click "New app"
   - Select your repository: `YOUR_USERNAME/product-os-war-room-simulation`
   - Main file path: `app.py`
   - Click "Deploy"

4. **Get Shareable URL**
   - Streamlit will deploy your app and give you a URL like:
     `https://YOUR_USERNAME-product-os-war-room-simulation-app-xxxxxx.streamlit.app`
   - Share this URL with TPMs during the simulation

### Deployment Notes

- Streamlit Cloud automatically detects `requirements.txt` and installs dependencies
- The app will redeploy automatically when you push changes to GitHub
- Free tier allows unlimited public apps
- Data files in `data/` folder are included in the deployment

---

## Running the Simulation

### Materials Needed

1. **Printed packets** (one per role per team):
   - Engineering Lead packet (8 pages)
   - Sales Lead packet (9 pages: 6 pages transcripts + 3 emails)
   - TPM gets laptop with dashboard URL

2. **Team worksheets** - Template for teams to record their selections

3. **Facilitator guide** - Run-of-show, timing, debrief script

### Simulation Flow (40 minutes)

1. **Setup** (5 min)
   - Divide 20 TPMs into 6-7 teams of 3
   - Assign roles: Engineering Lead, Sales Lead, TPM
   - Distribute role packets
   - Give TPM the dashboard URL

2. **Individual Review** (10 min)
   - Engineering Lead: Reviews feature catalog
   - Sales Lead: Reads customer transcripts and escalations
   - TPM: Explores analytics dashboard

3. **Team Discussion** (20 min)
   - Engineering presents feature options
   - Sales argues for urgent customer needs
   - TPM shares data findings
   - Team debates and selects 5 features within 100 points

4. **Scoring & Debrief** (5 min)
   - Reveal true ARR impact of each feature
   - Show optimal solution vs team selections
   - Discuss why manual signal processing failed

---

## Debrief Key Points

**What Went Wrong:**
- Teams focused on loud customers (MegaCorp, TechConf) instead of broad data
- Trap features felt urgent but had low impact
- Hidden gems were buried in boring analytics (page 2, tab 4, table row 15)
- Manual coordination was hard even with just 3 people and 14 features

**Why This Matters:**
- At scale (100+ features, 20+ stakeholders), manual process completely breaks
- "Loudest voice wins" prioritization misses high-impact opportunities
- This is why we need automated signal processing tools (VoC dashboards, research co-pilots)

**The Solution: Product Ops SENSE Pillar**
- Real-time VoC dashboards with LLM-powered tagging
- Automated pattern detection across support tickets, calls, surveys
- Quantified impact analysis (not just frequency, but ARR correlation)
- Proactive insights delivered to PMs instead of manual digging

---

## Files Not to Share with Participants

- `master-features-list.md` - Contains the answer key with true ARR impacts
- This README - Contains hints about hidden gems
- `PROJECT_JOURNAL.md` - Contains design rationale

---

## Questions or Issues?

Contact: Jason Yu (jyu@abnormalsecurity.com)
