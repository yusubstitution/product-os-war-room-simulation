# Master Features List - ANSWER KEY
**DO NOT SHARE WITH PARTICIPANTS**

This document contains the ground truth for all features in the simulation. Use this to build role-specific information packets.

---

## Feature Categories

- **TRAP** - High Noise, Low Signal (loud/urgent but low actual ARR impact)
- **HIDDEN GEM** - Low Noise, High Signal (buried in data but massive ARR impact)
- **DEFENSIBLE** - Medium Noise, Medium Signal (reasonable choices, moderate impact)
- **BAD IDEA** - Low Noise, Very Low Signal (obviously poor choices)

---

## TRAP FEATURES (High Noise, Low Signal)

### F01: Custom White-Label Mobile App for MegaCorp
**Category:** TRAP
**Story Points:** 35
**TRUE ARR Impact:** $800K (retention only, high opportunity cost)
**Noise Level:** VERY HIGH
**Workflow:** Event Creation & Setup

**Description:**
Build custom white-label mobile app for MegaCorp's annual conference with branded UI, offline mode, and custom integrations.

**The Noise (What Roles Will See):**
- **Sales:** MegaCorp ($800K ACV, 10% of enterprise ARR) escalation email from CEO: "Without branded mobile app, moving to Cvent"
- **Engineering:** Complex technical requirements, needs iOS/Android native development
- **TPM:** Only 3 customers ever requested custom mobile apps (buried in support data)

**The Signal (Hidden):**
- Saves $800K but costs 35 story points
- Only serves 1 customer's unique need
- Meanwhile, 40+ customers requested event cloning (18 points, broader impact)
- Mobile app maintenance = ongoing costs

**Why It's a Trap:** Hostage situation. Feels too urgent to ignore, but massive opportunity cost.

---

### F02: Advanced Networking Features (AI Matchmaking & Meeting Scheduler)
**Category:** TRAP
**Story Points:** 30
**TRUE ARR Impact:** $1M (might win 2-3 deals, but narrow segment)
**Noise Level:** VERY HIGH
**Workflow:** Event Delivery

**Description:**
AI-powered attendee matchmaking, 1:1 meeting scheduler, networking lounges, and interest-based recommendations.

**The Noise (What Roles Will See):**
- **Sales:** Lost TechConf deal ($500K ACV) because "Bizzabo has better networking." This appears in every Q4 competitive loss report
- **Engineering:** Technically interesting, good for recruiting/PR
- **TPM:** Only 12% of attendees use existing basic networking features (buried on page 18)

**The Signal (Hidden):**
- TechConf runs tech conferences where networking is critical (niche)
- 80% of EventFlow customers run webinars/workshops where networking isn't primary need
- Real churn driver: poor mobile registration (60% mobile traffic, 51% abandonment)

**Why It's a Trap:** One loud loss feels like pattern, but data shows it's not the real problem.

---

### F03: AI-Powered Event Content Generator
**Category:** TRAP
**Story Points:** 25
**TRUE ARR Impact:** Low adoption (<10% projected), high maintenance
**Noise Level:** HIGH
**Workflow:** Event Creation & Setup

**Description:**
AI writes session descriptions, event copy, promotional emails, and social posts using brand voice training.

**The Noise (What Roles Will See):**
- **Sales:** Prospects ask "Do you have AI features?" in every demo. Sounds strategic and modern
- **Engineering:** CPO presented this at exec offsite: "AI is the future of event management"
- **TPM:** Pilot survey shows only 15% of customers would use this (buried in survey appendix)

**The Signal (Hidden):**
- Customer interviews: Don't trust AI for brand voice
- Event templating/cloning has 200+ support tickets vs 5 mentions of AI content
- Real bottleneck: Multi-session setup takes 4+ hours due to no templating

**Why It's a Trap:** Executive pet project. Sounds innovative but customers won't adopt it.

---

## HIDDEN GEM FEATURES (Low Noise, High Signal)

### F04: Mobile Registration Flow Optimization
**Category:** HIDDEN GEM
**Story Points:** 20
**TRUE ARR Impact:** $4-6M (retention + expansion from better event outcomes)
**Noise Level:** LOW
**Workflow:** Registration & Marketing

**Description:**
Optimize registration flow for mobile devices: simplified forms, mobile-optimized payment, one-tap registration for returning attendees.

**The Noise (What Roles Will See):**
- **Sales:** A few mentions of "mobile is clunky" but no lost deals
- **Engineering:** Feels like optimization work, not innovation
- **TPM:** Has the golden data (but buried on page 12 of analytics deck)

**The Signal (Hidden in TPM Data):**
- 62% of registrations start on mobile
- Mobile abandonment: 51% vs 28% desktop
- 18,000 additional registrations/month if mobile matched desktop
- Retention correlation (requires scrolling below the fold): 10pp improvement in completion = 8.2pp increase in renewal rate
- Cohort analysis shows >75% completion = 87% renewal vs <60% = 73% renewal

**Why It's Hidden:** No drama, no escalations. Just boring funnel metrics in Tab 2. The retention correlation requires scrolling past the obvious abandonment chart to find the "Business Impact Analysis" section.

---

### F05: Event Cloning & Template System
**Category:** HIDDEN GEM
**Story Points:** 18
**TRUE ARR Impact:** $3-4M (retention + adoption, every customer benefits)
**Noise Level:** LOW
**Workflow:** Event Creation & Setup

**Description:**
One-click event duplication, custom template library, bulk editing for recurring events.

**The Noise (What Roles Will See):**
- **Sales:** Occasionally mentioned, but not deal-breakers
- **Engineering:** Straightforward to build, but feels like "nice to have"
- **TPM:** Has compelling data (but in boring support ticket analysis)

**The Signal (Hidden in TPM Data):**
- 247 support tickets in Q4 about "copy event," "duplicate," "template"
- Average setup time: 4.2 hours first-time, 3.1 hours repeat
- 78% of customers run similar events repeatedly
- Time-to-value: Customers who launch first event in <1hr have 40% higher 6-month retention

**Why It's Hidden:** Steady drumbeat of boring support tickets. No single loud customer.

---

### F06: Advanced Post-Event Analytics Dashboard
**Category:** HIDDEN GEM
**Story Points:** 25
**TRUE ARR Impact:** $5-7M (massive retention driver if non-users adopt)
**Noise Level:** LOW
**Workflow:** Post-Event Analytics & Follow-Up

**Description:**
Engagement scoring, ROI calculator, attendee journey visualization, automated insights, exportable executive summaries.

**The Noise (What Roles Will See):**
- **Sales:** No lost deals over analytics
- **Engineering:** Feels like reporting work, not exciting
- **TPM:** Has the smoking gun correlation (but buried on page 23)

**The Signal (Hidden in TPM Data):**
- Customers who view analytics ≥5 times/quarter: 95% retention
- Customers who view <5 times: 73% retention
- Only 31% currently use analytics regularly (69% opportunity)
- Exit surveys: "Can't prove ROI to leadership" = top churn reason

**Why It's Hidden:** Correlation in data table. No urgency, sounds like "nice to have reporting."

---

## DEFENSIBLE FEATURES (Medium Noise, Medium Signal)
*Engineering Lead's Original Roadmap = 100 points exactly*

### F07: API Rate Limit Increase & Webhook Reliability
**Category:** DEFENSIBLE
**Story Points:** 22
**TRUE ARR Impact:** $500K (prevents potential enterprise churn)
**Noise Level:** MEDIUM
**Workflow:** Technical Infrastructure

**Description:**
Increase API rate limits from 1000 to 5000 calls/hour, improve webhook delivery to 99.9% reliability.

**Customer Impact:**
- ~15 enterprise customers with heavy integrations benefit
- Moderate quality-of-life improvement
- Not blocking deals or causing churn currently

**Why Defensible:** Real technical debt, real value, just not highest ROI for 22 points.

---

### F08: Email Personalization Engine
**Category:** DEFENSIBLE
**Story Points:** 15
**TRUE ARR Impact:** $1M (improves satisfaction, modest retention bump)
**Noise Level:** MEDIUM
**Workflow:** Registration & Marketing

**Description:**
Dynamic email personalization using first name, company, ticket type, custom fields, conditional content blocks.

**Customer Impact:**
- 45 customer requests in backlog
- Competitive parity feature (most competitors have this)
- Improves email engagement rates
- Nice-to-have, not must-have

**Why Defensible:** Legitimate moderate-frequency request. Reasonable priority, just not most impactful.

---

### F09: Multi-Currency Support
**Category:** DEFENSIBLE
**Story Points:** 20
**TRUE ARR Impact:** $800K (international expansion, prevents some churn)
**Noise Level:** MEDIUM
**Workflow:** Registration & Marketing

**Description:**
Support ticket sales in 20+ currencies with automatic conversion, local payment methods.

**Customer Impact:**
- ~40 international customers benefit
- Enables expansion into EU/APAC markets
- Competitive gap vs Cvent/Bizzabo
- Workarounds exist (customers manage)

**Why Defensible:** Real gap, enables growth, just serves smaller segment than broader issues.

---

### F10: Speaker Portal Enhancements
**Category:** DEFENSIBLE
**Story Points:** 23
**TRUE ARR Impact:** $1.2M (appeals to conference organizers, modest expansion)
**Noise Level:** MEDIUM
**Workflow:** Event Delivery

**Description:**
Dedicated speaker portal with session uploads, bio management, Q&A dashboard, schedule coordination.

**Customer Impact:**
- ~60 customers run multi-speaker events
- Makes speaker management less manual
- Quality-of-life for conference organizers
- Not critical pain point

**Why Defensible:** Real need for conference segment, doesn't address bottlenecks for majority.

---

### F11: Real-Time Capacity Monitoring & Waitlist Automation
**Category:** DEFENSIBLE
**Story Points:** 20
**TRUE ARR Impact:** $600K (efficiency for power users, modest retention)
**Noise Level:** MEDIUM
**Workflow:** Registration & Marketing

**Description:**
Auto-notify organizers at 80% capacity, automatically promote waitlist attendees when spots open, smart waitlist prioritization.

**Customer Impact:**
- ~30 high-volume event organizers benefit
- Saves time on manual waitlist management
- Most events don't hit capacity (limited applicability)

**Why Defensible:** Solves real problem for subset, not broadest impact.

---

## BAD IDEA FEATURES (Low Noise, Very Low Signal)

### F12: VR/AR Event Experiences
**Category:** BAD IDEA
**Story Points:** 40
**TRUE ARR Impact:** ~$0 (maybe $100K from 1-2 bleeding-edge customers)
**Noise Level:** LOW
**Workflow:** Event Delivery

**Description:**
Virtual venue builder with 3D avatars, spatial audio, VR headset support, metaverse integration.

**Why It's Bad:**
- Requires VR headsets most attendees don't have
- Customer research: Only 3% expressed any interest
- Zero support tickets requesting this
- Market isn't ready (even Meta struggling with adoption)
- Massive complexity for near-zero usage

**Signal in Data:**
- TPM survey shows 3% interest
- Zero support tickets
- Sales: Mentioned in 2 calls (both said "interesting but not now")

---

### F13: Built-in Payment Processing
**Category:** BAD IDEA
**Story Points:** 35
**TRUE ARR Impact:** Negative (customers resist, compliance costs eat savings)
**Noise Level:** LOW
**Workflow:** Registration & Marketing

**Description:**
Proprietary payment processing system to replace Stripe integration, avoid 2.9% fees.

**Why It's Bad:**
- PCI DSS compliance nightmare
- Customers trust Stripe, would resist switching
- Ongoing maintenance burden (fraud, security, regulations)
- Stripe downtime affects 0.01% of transactions (not material)
- Only 4 support tickets mention Stripe issues

**Signal in Data:**
- 4 support tickets total (all resolved quickly)
- No customer requests to move off Stripe
- Engineering lead's cost-saving idea (not customer-driven)

---

### F14: Gamification & Achievement System
**Category:** BAD IDEA
**Story Points:** 25
**TRUE ARR Impact:** ~$200K (small niche of "fun" event organizers)
**Noise Level:** LOW
**Workflow:** Event Delivery

**Description:**
Badges, leaderboards, attendee "XP points" for engagement, achievement unlocks.

**Why It's Bad:**
- Only 8% of organizers said they'd use gamification
- Hopin tried this in 2023, had <5% adoption, killed it
- Wrong fit for professional B2B events (conferences, webinars)
- Adds UI clutter without clear ROI
- Risk: Makes platform feel less serious/professional

**Signal in Data:**
- 6 customer mentions in 12 months (all "nice to have someday")
- Customer interviews: Not a priority for B2B events
- Competitor failure data (Hopin killed after low adoption)

---

## OPTIMAL SOLUTION (Maximum ARR)

**Best 5-Feature Combination:**
1. F04: Mobile Registration Optimization - 20pts, $5M
2. F05: Event Cloning & Templates - 18pts, $3.5M
3. F06: Advanced Analytics Dashboard - 25pts, $6M
4. F08: Email Personalization - 15pts, $1M
5. F11: Capacity & Waitlist Automation - 20pts, $600K

**Total: 98 Story Points, ~$16.1M ARR Impact**

**Why This is Optimal:**
- All three Hidden Gems (massive broad impact)
- Two best Defensible features (reasonable additions)
- Addresses all four core workflows
- Serves all customer segments (Enterprise, Mid-Market, SMB)
- High retention drivers + adoption accelerators

---

## COMMON SUBOPTIMAL SELECTIONS

**Trap-Heavy Roadmap (Likely):**
- F01: MegaCorp Mobile App - 35pts, $800K
- F02: Networking Features - 30pts, $1M
- F08: Email Personalization - 15pts, $1M
- F11: Capacity & Waitlist - 20pts, $600K

**Total: 100 Points, ~$3.4M ARR** (Only 21% of optimal!)

**Engineering's Original Roadmap:**
- F07: API/Webhooks - 22pts, $500K
- F08: Email Personalization - 15pts, $1M
- F09: Multi-Currency - 20pts, $800K
- F10: Speaker Portal - 23pts, $1.2M
- F11: Capacity/Waitlist - 20pts, $600K

**Total: 100 Points, ~$4.1M ARR** (26% of optimal)

---

## NOTES FOR PACKET DESIGN

**Sales Lead should see:**
- Loud noise for F01 (MegaCorp escalation)
- Loud noise for F02 (TechConf loss)
- Some noise for F03 (prospects asking about AI)
- Minimal mention of F04-F06 (just casual "some customers mention this")

**Engineering Lead should see:**
- Their original roadmap (F07-F11) with rationale
- Technical complexity notes for all features
- Why they deprioritized the traps (too customer-specific, risky)
- Why they deprioritized hidden gems (seemed like optimization, not innovation)

**TPM should see:**
- Tab 2: Mobile registration funnel data + retention correlation (requires scrolling) (F04)
- Tab 3: Support ticket volume analysis (F05)
- Tab 4: Analytics usage vs retention correlation (F06)
- Scattered mentions of traps with low signal indicators (easy to miss)
- Data showing defensible features are solid but not optimal

---

**End of Master Features List**
