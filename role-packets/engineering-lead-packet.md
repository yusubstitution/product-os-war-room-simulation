# Engineering Lead Packet - Q1 2026 Feature Planning

**Confidential - For Planning Exercise Only**

---

## Your Role

You are the Engineering Lead for EventFlow. Your team spent the last month analyzing the backlog and developing a balanced roadmap for Q1 2026. You have 100 story points of capacity to allocate.

**Your Original Roadmap (F07-F11)** represents your team's best judgment based on technical priorities, customer requests, and strategic goals. However, Sales and the TPM may have different perspectives based on their data.

**Your Goal:** Work with Sales and TPM to select the optimal 5 features that fit within 100 story points.

---

## Complete Feature Catalog

All candidate features are listed below. Use this as your reference when discussing options with your team.

---

### WORKFLOW 1: EVENT CREATION & SETUP

#### F01: Custom White-Label Mobile App for MegaCorp
**Story Points:** 35

**Description:**
Build a fully custom white-label mobile app for MegaCorp's annual conference. Includes branded UI/UX, offline mode for poor connectivity, custom integrations with their internal systems, and separate iOS/Android native apps.

**Why So Many Points:**
- Requires native iOS and Android development (not web-based)
- Custom integrations with MegaCorp's proprietary systems
- Ongoing maintenance and app store management
- High technical risk - mobile apps are complex and require specialized skills
- One-off solution - not reusable for other customers

**Engineering Perspective:**
Your team initially deprioritized this because it's very customer-specific. Building custom solutions for single customers creates technical debt and doesn't scale. However, you understand Sales may feel differently if this customer is at risk.

---

#### F03: AI-Powered Event Content Generator
**Story Points:** 25

**Description:**
AI writes session descriptions, event copy, promotional emails, and social posts using brand voice training. Includes LLM integration, brand voice customization, content templates, and approval workflows.

**Why So Many Points:**
- LLM integration and prompt engineering
- Brand voice training system (requires ML expertise)
- Content review and approval workflows
- Ongoing AI model costs and maintenance
- Need to handle edge cases (inappropriate content, factual errors)

**Engineering Perspective:**
Your team deprioritized this because it felt like a "cool tech" project without clear customer validation. AI content generation is trendy but requires significant ongoing costs (LLM API fees) and maintenance. You're skeptical about adoption.

---

#### F05: Event Cloning & Template System
**Story Points:** 18

**Description:**
One-click event duplication, custom template library where organizers can save/reuse event setups, bulk editing for recurring events (e.g., weekly webinars with same format).

**Why So Many Points:**
- Database schema changes to support templates
- Complex UI for template management and customization
- Need to handle edge cases (what gets cloned vs. reset?)
- Bulk editing logic for recurring events
- Testing across many event configurations

**Engineering Perspective:**
Your team considered this but deprioritized it because it felt like "optimization work" rather than innovation. It's a solid quality-of-life feature but not strategically exciting.

---

### WORKFLOW 2: REGISTRATION & MARKETING

#### F04: Mobile Registration Flow Optimization
**Story Points:** 20

**Description:**
Optimize registration flow for mobile devices: simplified forms with fewer fields, mobile-optimized payment experience, one-tap registration for returning attendees, autofill integration, progress indicators.

**Why So Many Points:**
- Requires UX redesign and extensive mobile testing
- Payment flow changes (PCI compliance considerations)
- Integration with mobile autofill and password managers
- A/B testing framework to validate improvements
- Need to maintain backward compatibility with existing flows

**Engineering Perspective:**
Your team deprioritized this because it's optimization work on an existing feature. It's important, but mobile registration technically "works" today - it's not broken, just not optimal.

---

#### F08: Email Personalization Engine
**Story Points:** 15

**Description:**
Dynamic email personalization using first name, company, ticket type, custom fields, and conditional content blocks. Includes drag-and-drop email builder with personalization tokens.

**Why So Many Points:**
- Email template engine with conditional logic
- Drag-and-drop builder UI
- Testing framework (preview with sample data)
- Integration with existing email delivery system
- Edge case handling (missing fields, fallback values)

**Engineering Perspective:**
This is on your original roadmap (F08). It's a frequently requested feature with clear customer demand and moderate complexity. Good balance of value and effort.

---

#### F09: Multi-Currency Support
**Story Points:** 20

**Description:**
Support ticket sales in 20+ currencies with automatic conversion, local payment methods (e.g., iDEAL in Netherlands, Alipay in China), currency display throughout platform.

**Why So Many Points:**
- Integration with currency conversion APIs
- Payment gateway support for local methods
- Extensive testing across currencies and regions
- Edge cases (refunds, currency fluctuations, tax calculations)
- Ongoing maintenance for new currencies/payment methods

**Engineering Perspective:**
This is on your original roadmap (F09). It addresses a competitive gap and enables international expansion. Clear strategic value for growing in EU and APAC markets.

---

#### F11: Real-Time Capacity Monitoring & Waitlist Automation
**Story Points:** 20

**Description:**
Auto-notify organizers when events hit 80% capacity, automatically promote waitlist attendees when spots open, smart waitlist prioritization (e.g., VIP ticket holders first).

**Why So Many Points:**
- Real-time monitoring infrastructure (webhooks, notifications)
- Automated promotion logic with edge case handling
- Email automation for waitlist updates
- Admin dashboard for capacity management
- Testing for race conditions (multiple people claiming same spot)

**Engineering Perspective:**
This is on your original roadmap (F11). It solves a real operational pain point for high-volume organizers. Good automation candidate with clear rules-based logic.

---

#### F13: Built-in Payment Processing
**Story Points:** 35

**Description:**
Build proprietary payment processing system to replace Stripe integration. Handle credit card processing, fraud detection, PCI DSS compliance, refunds, and international payments.

**Why So Many Points:**
- PCI DSS Level 1 compliance (extremely complex and costly)
- Fraud detection and prevention systems
- International payment support (many countries, regulations)
- Ongoing security maintenance and audits
- Liability and financial risk management

**Engineering Perspective:**
Your team strongly recommends against this. Stripe is industry-standard and trusted. Building payment processing from scratch is a massive undertaking with ongoing compliance costs and risk. This is not core to EventFlow's value proposition.

---

### WORKFLOW 3: EVENT DELIVERY

#### F02: Advanced Networking Features (AI Matchmaking & Meeting Scheduler)
**Story Points:** 30

**Description:**
AI-powered attendee matchmaking based on interests/roles, 1:1 meeting scheduler with calendar integration, virtual networking lounges, interest-based recommendations.

**Why So Many Points:**
- AI matchmaking algorithm (requires ML expertise)
- Meeting scheduler with complex calendar integration (Google, Outlook, etc.)
- Real-time networking UI (chat, video, presence indicators)
- Recommendation engine based on attendee profiles
- Extensive testing for performance at scale (thousands of attendees)

**Engineering Perspective:**
Your team deprioritized this because it's technically complex and serves a narrow use case (primarily conferences, not webinars). Most EventFlow customers run webinars where networking isn't the primary value proposition.

---

#### F10: Speaker Portal Enhancements
**Story Points:** 23

**Description:**
Dedicated speaker portal with session material uploads (slides, videos), bio and headshot management, Q&A dashboard for speaker-attendee interaction, schedule coordination.

**Why So Many Points:**
- Separate portal UI with authentication and permissions
- File upload and storage infrastructure
- Q&A system with moderation and notifications
- Calendar/schedule integration
- Email automation for speaker communications

**Engineering Perspective:**
This is on your original roadmap (F10). It's a solid feature for conference organizers who manage multiple speakers. Addresses a clear pain point with moderate complexity.

---

#### F12: VR/AR Event Experiences
**Story Points:** 40

**Description:**
Virtual venue builder with 3D avatars, spatial audio, VR headset support (Meta Quest, HTC Vive), metaverse integration, immersive event experiences.

**Why So Many Points:**
- Requires 3D graphics expertise (Unity or Unreal Engine)
- VR hardware integration and testing
- Performance optimization for different devices
- Spatial audio and networking infrastructure
- Bleeding-edge technology with limited browser support

**Engineering Perspective:**
Your team strongly recommends against this. VR/AR for events is not market-ready - adoption is extremely low, requires specialized hardware, and is very expensive to build and maintain. This feels like a science project, not a product feature.

---

#### F14: Gamification & Achievement System
**Story Points:** 25

**Description:**
Badges, leaderboards, attendee "XP points" for engagement actions (attending sessions, asking questions, networking), achievement unlocks, social sharing.

**Why So Many Points:**
- Gamification engine with point tracking and rules
- Leaderboard infrastructure (real-time updates, privacy considerations)
- Badge design and achievement logic
- Social sharing integrations
- Admin controls for organizers to customize gamification

**Engineering Perspective:**
Your team deprioritized this because customer feedback was lukewarm. Gamification works well for consumer apps but feels awkward for professional B2B events. Risk of making the platform feel less serious.

---

### WORKFLOW 4: POST-EVENT ANALYTICS & FOLLOW-UP

#### F06: Advanced Post-Event Analytics Dashboard
**Story Points:** 25

**Description:**
Engagement scoring for attendees (who was most engaged?), ROI calculator showing event value, attendee journey visualization (registration → check-in → sessions → follow-up), automated insights, exportable executive summaries.

**Why So Many Points:**
- Complex data aggregation and analysis
- Data visualization dashboard with interactive charts
- ROI calculation logic (requires business logic and formulas)
- Automated insight generation (pattern detection)
- Executive summary export (PDF generation with branded templates)

**Engineering Perspective:**
Your team considered this but deprioritized it because analytics felt like "reporting work" rather than core product innovation. You recognize it's important but doesn't feel strategically exciting compared to new capabilities.

---

#### F07: API Rate Limit Increase & Webhook Reliability
**Story Points:** 22

**Description:**
Increase API rate limits from 1000 to 5000 calls/hour, improve webhook delivery reliability to 99.9% uptime, add webhook retry logic and monitoring dashboard.

**Why So Many Points:**
- Infrastructure scaling (load testing, capacity planning)
- Webhook retry logic with exponential backoff
- Monitoring and alerting system
- Documentation updates and customer communications
- Testing with high-volume API customers

**Engineering Perspective:**
This is on your original roadmap (F07). It's technical debt that's been on the backlog for months. A few enterprise customers occasionally hit rate limits, and webhook failures create support tickets. Feels like "good engineering" - improve platform stability.

---

## Your Original Q1 2026 Roadmap

Your team spent a month analyzing the backlog and created this roadmap. It represents your best judgment based on:
- Customer request frequency
- Technical debt priorities
- Competitive gaps
- Strategic goals (international expansion, conference market)

### Proposed Features (100 Story Points)

1. **F07: API Rate Limit & Webhook Reliability** - 22 points
   - **Why:** Technical debt, enterprise customer need, platform stability

2. **F08: Email Personalization Engine** - 15 points
   - **Why:** Frequently requested (45+ requests), competitive parity, clear value

3. **F09: Multi-Currency Support** - 20 points
   - **Why:** Competitive gap, enables international expansion, strategic

4. **F10: Speaker Portal Enhancements** - 23 points
   - **Why:** Differentiates in conference segment, clear customer need

5. **F11: Capacity Monitoring & Waitlist Automation** - 20 points
   - **Why:** Solves operational pain for power users, good automation candidate

**Total: 100 Story Points**

---

## Your Talking Points for the Discussion

**Why you're confident in this roadmap:**
- Balanced approach: technical debt + customer requests + strategic bets
- Addresses multiple customer segments (enterprise, international, conferences)
- Moderate risk - all features are well-scoped and achievable
- No single-customer solutions or bleeding-edge tech experiments

**Potential pushback you expect:**
- **Sales may push for customer-specific features** (e.g., F01 for MegaCorp)
  - Your response: "That's a one-off solution that doesn't scale. We'd create technical debt for one customer."
- **Sales may want competitive features** (e.g., F02 networking, F03 AI)
  - Your response: "We need to see stronger customer validation before investing 25-30 story points."
- **TPM may have data** showing different priorities
  - Your response: "I'm open to data-driven reprioritization if the numbers are compelling."

**What would make you change your mind:**
- Strong quantitative data showing hidden opportunities (e.g., retention correlations, usage patterns)
- Evidence that your roadmap misses a major customer pain point
- Clear ARR impact projections that differ significantly from your assumptions

---

## Instructions for the Simulation

1. **Present your roadmap** (5 min): Walk your team through the feature catalog and your original roadmap (F07-F11)

2. **Listen to Sales and TPM** (10 min): Let Sales present their escalations and customer feedback. Let TPM share their analytics.

3. **Debate and decide** (15 min): Work with your team to select 5 features that fit within 100 story points. You can:
   - Keep your original roadmap
   - Adjust based on Sales/TPM input
   - Compromise to balance perspectives

4. **Fill out the worksheet**: List your final 5 features and story point total

---

**Remember:** Your job is to bring technical perspective and pushback on unrealistic or risky features. But you should also be open to data-driven reprioritization if Sales or TPM have compelling evidence.

Good luck!
