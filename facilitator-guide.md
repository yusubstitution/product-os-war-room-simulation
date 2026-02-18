# Facilitator Guide - Product OS War Room Simulation

**Simulation Goal:** Demonstrate that manual signal processing fails at scale by having TPM teams prioritize features from disconnected, messy data sources.

**Expected Outcome:** Most teams will select suboptimal roadmaps (~$3-4M ARR) because they're distracted by "Noise" (loud customers, exec escalations) and miss the "Signal" (boring data with high impact).

**Optimal Solution:** ~$16M ARR (teams typically achieve only 20-25% of optimal)

---

## Pre-Simulation Setup (30 minutes before)

### Room Setup

- [ ] **Tables:** Arrange 6-7 tables for teams of 3
- [ ] **Projector/Screen:** For debrief presentation
- [ ] **WiFi:** Confirm strong connection for dashboard access
- [ ] **Whiteboard:** To write dashboard URL

### Materials Checklist

**Printed Materials (6-7 sets):**
- [ ] Engineering Lead packet (8 pages each) - `role-packets/engineering-lead-packet.md`
- [ ] Sales Lead packet (9 pages each) - `role-packets/sales-lead-packet.md`
- [ ] TPM instructions (2 pages each) - `role-packets/tpm-packet-instructions.md`
- [ ] Team worksheets (1 per team) - `team-worksheet.md`
- [ ] Pens/markers for worksheets

**Digital:**
- [ ] Dashboard URL accessible: https://appuct-os-war-room-simulation-gzuxkhqjlfrfmbh5nhfhsy.streamlit.app/
- [ ] Test dashboard on venue WiFi
- [ ] Laptops/tablets for TPMs (1 per team) with dashboard loaded
- [ ] Answer key ready: `master-features-list.md`
- [ ] Debrief slides or whiteboard prepared

### Pre-Check

- [ ] Dashboard loads properly (check all 5 tabs)
- [ ] All role packets printed and organized by role
- [ ] Team worksheets have pens
- [ ] Timer or clock visible
- [ ] Your answer key is handy but not visible to participants

---

## Simulation Overview

**Total Time:** 40 minutes
- 5 min: Introduction and team formation
- 10 min: Individual review
- 20 min: Team discussion and selection
- 5 min: Submission and quick poll

**Debrief:** 15-20 minutes
- Reveal true ARR impacts
- Show optimal solution
- Discuss why manual processing fails
- Connect to Product Ops SENSE pillar

---

## Run of Show

### Phase 1: Introduction (5 minutes)

**Script:**

> "Welcome to the Product OS War Room! Today you're going to experience firsthand why manual signal processing breaks down at scale.
>
> **The Scenario:** You work for EventFlow, an event management SaaS company. You're planning Q1 2026 features. You have 100 story points of engineering capacity and 14 candidate features to choose from.
>
> **Your Goal:** Select the 5 features that maximize ARR impact while staying within 100 story points.
>
> **The Catch:** Each of you will get different information. Engineering has the feature catalog. Sales has customer escalations and deal losses. TPM has analytics data. You'll need to coordinate to make the best decision."

**Team Formation:**

- Divide 20 TPMs into 6-7 teams of 3
- Assign roles within each team:
  - 1 Engineering Lead (gets feature catalog)
  - 1 Sales Lead (gets customer transcripts and escalations)
  - 1 TPM (gets dashboard URL and laptop)

**Distribute Materials:**

- Hand out role packets to each person
- Give TPMs laptops/tablets with dashboard URL
- Write dashboard URL on whiteboard: https://appuct-os-war-room-simulation-gzuxkhqjlfrfmbh5nhfhsy.streamlit.app/
- Give each team one worksheet

**Set Expectations:**

> "You'll have 10 minutes to review your materials individually, then 20 minutes to discuss as a team and make your selections. This is time-boxed on purpose - in real life, you don't have unlimited time to reconcile data.
>
> At the end, we'll reveal the true ARR impact of each feature and see how your selections compare to the optimal solution."

---

### Phase 2: Individual Review (10 minutes)

**Instructions to Participants:**

> "Take the next 10 minutes to review your materials. Don't discuss with your teammates yet - just read and take notes.
>
> - **Engineering Lead:** Review the feature catalog. Understand what each feature does and why your team originally proposed your 100-point roadmap.
> - **Sales Lead:** Read the customer transcripts and escalation emails. Pay attention to what customers are demanding and why they're urgent.
> - **TPM:** Explore the analytics dashboard. Click through all 5 tabs. Look for patterns in the data.
>
> Timer starts now!"

**Facilitator Actions:**

- Start 10-minute timer
- Walk around the room
- Answer clarifying questions about the simulation rules (but don't give hints!)
- Watch for common behaviors:
  - TPMs clicking through dashboard (good!)
  - Sales Leads highlighting urgent escalations (expected)
  - Engineering Leads reading their original roadmap rationale

**At 8 minutes:**
> "2 minutes remaining for individual review."

**At 10 minutes:**
> "Time's up! Now you have 20 minutes to discuss as a team and fill out your worksheet."

---

### Phase 3: Team Discussion & Selection (20 minutes)

**Instructions to Participants:**

> "Now work together as a team. Share what you learned from your materials and decide on 5 features.
>
> Remember:
> - You must stay within 100 story points total
> - Select exactly 5 features
> - Write your selections on the team worksheet
> - There's no single 'right' answer, but there is an optimal solution based on the data
>
> Timer starts now!"

**Facilitator Actions:**

- Start 20-minute timer
- Walk around and observe team dynamics (don't intervene!)
- **Watch for these patterns:**
  - Sales pushing hard for MegaCorp mobile app (Trap #1)
  - Sales arguing about TechConf networking features (Trap #2)
  - Engineering defending their original roadmap (5 defensible features)
  - TPMs trying to share data but getting talked over
  - Teams focusing on loud escalations vs boring metrics
  - Time pressure causing rushed decisions

**Common Discussions You'll Overhear:**

- "We can't lose MegaCorp - that's $800K!"
- "Networking features came up in 4 competitive losses"
- "The CEO asked about AI features"
- "But what do the numbers say?"
- "We don't have time to look at all the data"

**At 15 minutes:**
> "5 minutes remaining. Make sure your worksheet is filled out."

**At 18 minutes:**
> "2 minutes remaining. Finalize your selections."

**At 20 minutes:**
> "Time's up! Pens down. Please pass your worksheets forward."

---

### Phase 4: Quick Poll (3 minutes)

**Before the debrief, gather quick data:**

> "Quick poll - raise your hand if your team selected..."

Go through the traps:
- **F01: MegaCorp Custom Mobile App** (expect 60-80% of teams)
- **F02: Networking Features** (expect 40-60% of teams)
- **F03: AI Content Generator** (expect 20-40% of teams)

> "Interesting! Now let's see how these features actually stack up."

---

## Debrief (15-20 minutes)

This is where the learning happens. Take your time here.

### Step 1: Reveal the Answer (5 minutes)

**Display the optimal solution:**

> "Here's the optimal 5-feature roadmap based on the data you had access to:"

**Optimal Solution:**
1. **F04: Mobile Registration Optimization** - 20 pts, $5M ARR impact
2. **F05: Event Cloning & Templates** - 18 pts, $3.5M ARR impact
3. **F06: Advanced Analytics Dashboard** - 25 pts, $6M ARR impact
4. **F08: Email Personalization** - 15 pts, $1M ARR impact
5. **F11: Capacity & Waitlist Automation** - 20 pts, $600K ARR impact

**Total: 98 story points, ~$16.1M ARR impact**

> "Now let's calculate each team's total ARR and see how you did."

**Go through each team's worksheet:**
- Read their selections
- Calculate total ARR using the answer key
- Write on whiteboard

**Typical Results:**
- Team ARR: $2.5M - $5M
- Optimal: $16.1M
- Teams achieve: 15-30% of optimal

---

### Step 2: "Where Was the Signal?" (5 minutes)

**Show where the hidden gems were buried:**

> "Let's talk about those top 3 features - the 'hidden gems' worth $14.5M combined. Where was this information?"

**F04: Mobile Registration Optimization ($5M)**

> "This was in the TPM dashboard, Tab 2: Registration Funnel Analysis.
>
> The data showed:
> - 62% of registrations happen on mobile
> - Mobile abandonment: 51% vs Desktop: 28%
> - 18,000 lost registrations per month
>
> **But here's the problem:** No customer was screaming about this. It was just boring funnel metrics on page 2 of the dashboard. Easy to overlook when Sales is yelling about MegaCorp."

**F05: Event Cloning & Templates ($3.5M)**

> "This was buried in Tab 3: Support Tickets.
>
> The data showed 247 tickets in Q4 about event cloning - the 2nd highest category after login issues.
>
> **The hints were there:** In the customer transcripts, Sarah from MegaCorp mentioned 'wish we could copy last year's event.' Kevin from TechConf said 'I spent 3 hours setting up, wish I could clone.' But these were throwaway comments in long transcripts, easy to miss when they're also demanding custom mobile apps and networking features."

**F06: Advanced Analytics Dashboard ($6M)**

> "This was the golden correlation in Tab 4: Feature Usage & Retention.
>
> The data showed:
> - Customers who use analytics ≥5 times/quarter: 95% retention
> - Customers who don't: 73% retention
> - Only 31% currently use analytics (huge opportunity!)
>
> **But:** No one lost a deal over analytics. No exec escalations. Just a correlation table on page 4 of the dashboard."

---

### Step 3: "Why Did Teams Pick Traps?" (5 minutes)

**Walk through the traps:**

> "Now let's talk about the features many of you picked that actually had low ARR impact."

**F01: MegaCorp Custom Mobile App (35 pts, $800K)**

> "Show of hands - who picked this one? Most of you, right?
>
> **Why it felt urgent:**
> - CEO escalation email
> - $800K renewal at risk (10% of enterprise revenue!)
> - Deadline: Mid-February or they go to Cvent
>
> **The trap:**
> - Only serves 1 customer's unique need
> - Only 3 customers ever requested custom mobile apps (buried in TPM support ticket data)
> - Meanwhile, mobile registration optimization (F04) helps ALL customers and is worth $5M
>
> You spent 35 story points to save $800K when you could have spent 20 points to generate $5M."

**F02: Networking Features (30 pts, $1M)**

> "This one felt like a pattern, right? Lost TechConf deal, 4 competitive losses in Q4.
>
> **The trap:**
> - TechConf runs tech conferences where networking is critical (niche use case)
> - 80% of EventFlow customers run webinars/workshops where networking isn't the primary value
> - Only 12% of attendees use existing networking features (buried in TPM dashboard)
>
> One loud loss that felt like a trend, but the data showed it was a narrow segment problem."

**F03: AI Content Generator (25 pts, low adoption)**

> "AI is the future, right? Prospects ask about it in every demo. The CPO presented it at the exec offsite.
>
> **The trap:**
> - Pilot survey: Only 15% of customers said they'd use it (buried in TPM data)
> - Customers don't trust AI for brand voice
> - Event cloning (F05) solves the real time-saver problem - 247 tickets vs 5 mentions of AI
>
> Shiny and strategic-sounding, but customers won't adopt it."

---

### Step 4: "Why Manual Signal Processing Fails" (5 minutes)

**Key Teaching Points:**

> "So what just happened here? You're all smart, experienced TPMs. You had all the data. Why did most teams miss the optimal solution?
>
> Here are the patterns we saw:

**1. Loudest Voice Wins**
> "The urgent escalations (MegaCorp CEO email, lost deal reports) felt more real than boring analytics. Human nature: we respond to emotional urgency over statistical patterns."

**2. Information Asymmetry**
> "Each role had different pieces of the puzzle. Sales had escalations but not usage data. TPM had analytics but not customer context. Engineering had features but not ARR impact.
>
> Coordinating this information manually under time pressure is hard - even with just 3 people and 14 features!"

**3. Time Pressure Forces Gut Decisions**
> "You had 20 minutes. Not enough time to deeply analyze 5 tabs of dashboard data, read 6 pages of transcripts, and debate 14 features. So you defaulted to what felt urgent."

**4. Hidden Gems Are Boring**
> "The highest-impact features were buried in:
> - Page 2 of a dashboard (registration funnel)
> - A frequency table in Tab 3 (support tickets)
> - A correlation chart on page 4 (retention data)
>
> No drama. No exec pressure. Just... data. Easy to overlook."

**5. Scale Makes This Impossible**
> "Now imagine this at real scale:
> - 100+ features in the backlog
> - 20+ stakeholders with opinions
> - Dozens of customer conversations per week
> - Support tickets, surveys, product analytics, sales calls
>
> Manual signal processing completely breaks down. You can't read everything, so you respond to what's loud - which is often not what's most impactful."

---

### Step 5: Connect to Product Ops SENSE Pillar (3 minutes)

**The Solution:**

> "This is why we're building the Product Ops SENSE pillar. The goal is to replace manual signal processing with automated tools:

**What SENSE Does:**

1. **Real-Time VoC Dashboards**
   - LLM-powered tagging of support tickets, customer calls, surveys
   - Automatically surfaces patterns like '247 tickets about event cloning'
   - Quantifies impact, not just frequency

2. **Research Co-Pilots**
   - Searchable insight libraries
   - Auto-generate summaries of themes across customer conversations
   - Flag high-impact pain points buried in boring data

3. **Proactive Anomaly Detection**
   - Spot bottlenecks in product funnels (like mobile registration abandonment)
   - Alert PMs to retention correlations (like analytics usage → 95% retention)
   - Surface signal before it becomes a crisis

**The Key Shift:**
> "AI handles the 'what' - gathering feedback, tagging issues, finding patterns.
> Humans focus on the 'so what' - insights, prioritization, strategic decisions.
>
> Instead of TPMs manually digging through dashboards for 20 minutes under time pressure, the system proactively says: 'Hey, mobile registration has a massive opportunity - 18,000 lost registrations/month. Here's the data.'"

---

### Step 6: Q&A and Reflection (2-3 minutes)

**Open the floor:**

> "Questions? Reactions? What surprised you about this exercise?"

**Common Questions:**

**Q: "But wouldn't we eventually find the signal in real life?"**
> A: "Maybe, but at what cost? By the time you realize mobile registration is the issue, you've already spent 35 points on MegaCorp's custom app. In a real roadmap, those story points are gone. The opportunity cost is real."

**Q: "Aren't customer escalations important?"**
> A: "Yes! But they're one input, not the only input. MegaCorp's needs are valid, but they shouldn't override data showing a $5M opportunity that helps all customers. The goal is to balance loud urgency with quiet impact."

**Q: "How do we avoid falling for traps in real life?"**
> A: "Three things:
> 1. Build tools that surface signal proactively (SENSE pillar)
> 2. Force yourself to look at boring data, not just urgent escalations
> 3. Ask 'How many customers does this affect?' and 'What's the quantified impact?'"

---

## Facilitator Tips

### Managing Time
- Be strict with timers - time pressure is part of the lesson
- If teams finish worksheets early, encourage them to double-check their reasoning
- If running long, you can shorten the debrief Q&A

### Handling Questions During Simulation
- **Clarifying rules:** Answer freely (e.g., "Yes, you can pick any 5 features")
- **Hints about features:** Don't give them! (e.g., "Should we pick MegaCorp?" → "That's for your team to decide")
- **Technical issues:** Help immediately (dashboard won't load, can't find data)

### Reading the Room
- **If teams are struggling:** That's good! The struggle is the point
- **If Sales dominates discussion:** Normal - watch TPMs trying to get data heard
- **If Engineering is defensive:** Expected - they planned that roadmap for a month
- **If teams finish too quickly:** They probably didn't dig into the data

### Common Facilitation Mistakes
- ❌ Giving hints during team discussion ("Have you looked at Tab 4?")
- ❌ Rushing the debrief - this is where the learning happens
- ❌ Being judgmental ("You picked wrong!") - frame as "this is hard!"
- ❌ Skipping the SENSE pillar connection - that's the whole point

---

## Materials You'll Need

**To Print:**
- This facilitator guide (for you)
- 6-7 copies of Engineering Lead packet (8 pages each)
- 6-7 copies of Sales Lead packet (9 pages each)
- 6-7 copies of TPM instructions (2 pages each)
- 6-7 team worksheets
- Answer key (master-features-list.md) - FOR YOUR EYES ONLY

**Digital:**
- Dashboard: https://appuct-os-war-room-simulation-gzuxkhqjlfrfmbh5nhfhsy.streamlit.app/
- 6-7 laptops/tablets for TPMs
- Debrief slides (optional) or whiteboard to write results

---

## Post-Simulation

**Collect:**
- Team worksheets (for documentation)
- Feedback from TPMs (optional survey)

**Follow-Up:**
- Share simulation results in Slack or email
- Reference this exercise when discussing SENSE pillar projects
- Consider running again for other teams (PM, Eng, PMM)

---

## Troubleshooting

**Dashboard won't load:**
- Check WiFi connection
- Try refreshing the page
- Use mobile hotspot as backup
- Worst case: Share screenshots of key tabs

**Teams finish too early (before 20 min):**
- Ask: "Did you explore all 5 tabs of the dashboard?"
- Encourage: "Double-check your math - does it total ≤100 points?"

**Teams are stuck/paralyzed:**
- At 10 min mark: "You're halfway through. Don't overthink it - make your best call."
- Remind: "There's no perfect answer. Do your best with the data you have."

**Technical issues:**
- Have printed screenshots of key dashboard tabs as backup
- Worst case: Have TPM read from printed data tables

---

## Success Metrics

**The simulation is successful if:**
- ✅ Most teams select suboptimal roadmaps (proves the point!)
- ✅ Teams pick 2-3 traps on average
- ✅ In debrief, TPMs have "aha moments" about signal vs noise
- ✅ Connection to SENSE pillar feels relevant and actionable

**It's NOT about:**
- ❌ Teams getting the "right answer"
- ❌ Proving TPMs are bad at prioritization
- ❌ Criticizing individual decisions

**It IS about:**
- ✅ Experiencing how manual signal processing fails at scale
- ✅ Understanding why Product Ops tools are needed
- ✅ Building empathy for the messy reality of product decisions

---

## Questions?

Contact: Jason Yu (jyu@abnormalsecurity.com, Slack: @Jason Yu)

Good luck with the simulation! 🚀
