# Error Assessment: Annotator Disagreement Analysis

**Date:** November 19, 2025

## Overview

After conducting an annotation exercise with two additional annotators (Person A and Person B), I analyzed cases where annotators disagreed. Out of 40 total posts (20 from each subreddit), we achieved:
- **Complete agreement (3/3):** 27 posts (67.5%)
- **Majority agreement (2/3):** 13 posts (32.5%)
- **No agreement:** 0 posts (0%)

Overall, we achieved 100% majority agreement, meaning every post had at least 2 out of 3 annotators agreeing. This document examines the sources of disagreement and what they reveal about the taxonomy.

---

## Sources of Disagreement

### 1. **Social vs. Campus Services for Recommendation/Opinion Posts**

**Examples:**
- "Best pizza place near campus" (Me & Person B: Social | Person A: Campus Services)
- "Best pizza place in campus" (Me & Person B: Social | Person A: Campus Services)
- "Where do people print stickers around here?" (Me & Person A: Campus Services | Person B: Social)
- "Is Grey Nuns reading room incredibly cold?" (Me & Person A: Campus Services | Person B: Social)

**Analysis:**  
The most frequent disagreement was distinguishing between casual recommendations/opinions (Social) and actual service-related inquiries (Campus Services). Person A tended to code any campus-related question as Campus Services, while Person B interpreted casual tone as Social.

**Why this happened:**
- "Best pizza place" sounds like a casual recommendation request, but it involves campus food services
- "Where to print stickers" could be seen as either asking about a campus service or just community knowledge-sharing
- "Is the reading room cold" mixes facility question with subjective experience
- The line between "I need service information" and "What's your opinion about this campus thing?" is fuzzy

**Suggested improvement:** Clarify that opinion-seeking posts ("best," "worth it," subjective experience) should be coded as Social, while factual service questions ("is it open," "how do I access") are Campus Services.

---

### 2. **Course Content vs. Academic Planning/Support**

**Examples:**
- "Prof inputted wrong grade on my courses" (Me & Person B: Academic Planning | Person A: Course Content)
- "Introduction to Quantitative Political Science. - POLI 311 with Aaron Erlich" (Me & Person A: Course Content | Person B: Academic Planning)
- "I Failed my biol 200 midterm" (Me & Person A: Course Content | Person B: Academic Support)

**Analysis:**  
Posts that mention courses but focus on administrative issues or emotional reactions caused disagreement about whether they're about course content, planning, or support.

**Why this happened:**
- "Prof inputted wrong grade" mentions grades (Course Content territory) but is really about fixing an administrative error (Academic Planning)
- A post with a course code and professor name could be asking about content OR seeking course selection advice
- "I failed my midterm" mentions course performance but could be seeking emotional support rather than discussing content
- The taxonomy distinguishes these well in theory, but real posts mix multiple elements

**Suggested improvement:** Add guidance: if the main issue is administrative (grade corrections, registration) → Academic Planning; if discussing actual exam/assignment content → Course Content; if expressing struggle and seeking help → Academic Support.

---

### 3. **Ambiguous or Context-Dependent Posts**

**Examples:**
- "Me're all class traitors." (Me & Person B: Social | Person A: Student Governance)
- "SAE" (Me & Person A: Social | Person B: Academic Planning)
- "Going backwards to retake classes" (Me & Person A: Academic Planning | Person B: Social)
- "Question AFE bursary" (Me & Person B: Academic Planning | Person A: Campus Services)
- "Math Minor worth it?" (Me & Person A: Academic Planning | Person B: Social)

**Analysis:**  
Some posts lacked enough context to definitively determine category, leading to different interpretations of intent.

**Why this happened:**
- "Me're all class traitors" could be social commentary OR political statement about student unions
- "SAE" (Society of Automotive Engineers?) is too vague - could be a club (Social) or academic program question
- "Going backwards to retake classes" could be about system navigation OR venting frustration
- "AFE bursary" could be financial aid (service) or academic planning (funding for education)
- "Math Minor worth it?" is opinion-seeking (Social tendency) but about academic decisions (Planning)
- Very brief posts leave intent unclear

**Suggested improvement:** For ambiguous posts, default to the most specific applicable category. For opinion questions about academic decisions, prioritize Academic Planning over Social.

---

### 4. **Student Governance vs. Social for SSMU/CSU References**

**Examples:**
- "life if i never got another ssmu email ever again" (Me & Person A: Social | Person B: Student Governance)
- "Is there an Electrical Engineering Helpline community" (Me & Person A: Academic Support | Person B: Campus Services)

**Analysis:**  
Mentions of student organizations (SSMU, CSU) sometimes triggered Student Governance classification even when the post was really just casual commentary or resource questions.

**Why this happened:**
- Mentioning SSMU doesn't always mean the post is ABOUT student governance
- "life if i never got another ssmu email" is clearly venting/humor, not discussing governance
- Person B appeared to use keywords (SSMU, CSU) as primary classification signals
- The difference between "discussing student government" vs. "mentioning it in passing" wasn't clear

**Suggested improvement:** Specify that Student Governance requires the post to be ABOUT elections, policies, or official union activities - not just mentioning the organization.

---

### 5. **Annotator Experience and Interpretation Style**

**Observation:**  
Different annotators showed distinct patterns:

**Person A** (CS student, frequent Reddit user):
- More likely to interpret campus-related questions as Campus Services
- Tended toward literal interpretation of keywords
- Less likely to code things as Social
- More aligned with Me on Course Content distinctions

**Person B** (less familiar with university subreddits):
- More likely to code conversational/opinion posts as Social
- Sometimes confused service questions with social discussion
- Occasionally misidentified academic decisions as Social chat
- Less consistent with domain-specific distinctions

**Why this matters:**  
Annotator familiarity with university subreddit culture affects classification. Person B's unfamiliarity led to:
- Treating academic planning questions as casual conversation
- Missing the implicit purpose behind posts (e.g., "Math Minor worth it" is planning, not just chatting)
- Over-reliance on tone rather than function

**Impact:** Most disagreements involved Person B's classifications, suggesting the guide needs clearer examples that don't assume domain knowledge.

---

## Patterns in Complete Agreement

Posts with complete agreement (27/40 = 67.5%) tended to have:
- **Explicit course codes with clear assessment mentions** → Course Content
  - "PSYC337 midterm", "ECON230 midterm", "Phys 204 final"
- **Obvious requests for academic help** → Academic Support
  - "I need a tutor for ELEC 251 or I might end it"
- **Clear administrative/planning questions** → Academic Planning
  - "Can conditional standing apply for graduation?"
  - "How do I vote in the CSU elections?"
  - "Masters in public policy and administration MPPAA"
- **Unambiguous facility/service questions** → Campus Services
  - "STM STRIKE SUSPENDED?!"
  - "How to book a room in bronfman (3rd floor)"
- **Obviously casual/social content** → Social
  - "Thoughts?"
  - "McGill Speedcube Club is here!"
  - "Some of Me guys can't stop vomiting words for 50 mins"
- **Clear housing and employment posts** were unanimously agreed upon

Posts with disagreement (13/40 = 32.5%) tended to have:
- Opinion-seeking language about campus things
- Mentions of organizations without clear governance focus
- Mixed signals (course code + administrative issue)
- Ambiguous brevity or vague context
- Tone that could be read as either functional or conversational

---

## Recommendations for Taxonomy Improvement

1. **Add explicit decision rules for common ambiguities:**
   - "Opinion/recommendation posts about campus → Social (e.g., 'best pizza place')"
   - "Factual service questions → Campus Services (e.g., 'is it open?')"
   - "Posts mentioning student orgs are only Student Governance if ABOUT governance activities"
   - "Grade errors/admin issues → Academic Planning, even if they mention courses"

2. **Expand the Social category definition** to explicitly include:
   - Recommendation requests ("best X")
   - Opinion questions ("worth it?")
   - Venting or casual commentary
   - Community reactions and discussions

3. **Add more edge case examples** in the guide:
   - Include actual disagreement cases with explanations
   - Show why "Best pizza place" ≠ Campus Services
   - Demonstrate "Failed midterm" vs. "Need tutor" distinction

4. **Provide a decision tree** for annotators:
   ```
   Does it mention a course code?
   └─ Yes → Is it about assessment/content? → Course Content
       └─ Is it asking for help? → Academic Support
       └─ Is it an admin issue? → Academic Planning
   └─ No → Continue with other categories...
   ```

5. **Include training calibration phase:**
   - Have annotators code 5 practice posts together
   - Discuss disagreements before independent coding
   - This would especially help less experienced annotators like Person B

6. **Clarify keyword vs. intent:**
   - Mentioning SSMU ≠ automatically Student Governance
   - Course code ≠ automatically Course Content
   - Campus location ≠ automatically Campus Services
   - Intent and function matter more than keywords

---

## Conclusion

The annotation exercise revealed that while the taxonomy has solid theoretical foundations, real-world application produces systematic disagreements in predictable areas. The 13 disagreements (32.5% of posts) primarily stemmed from:

1. **Social vs. Campus Services ambiguity** - Opinion/recommendation posts about campus facilities
2. **Course mentions triggering automatic classifications** - Not considering the post's actual purpose
3. **Vague posts lacking context** - Brief titles that could mean multiple things
4. **Keyword-based vs. intent-based coding** - Some annotators relied too heavily on trigger words
5. **Domain expertise gaps** - Less familiar annotators struggled with implicit conventions

Despite these challenges, achieving 100% majority agreement (40/40 posts had at least 2/3 agreement) demonstrates the taxonomy is fundamentally sound and usable. The disagreements are concentrated in specific, identifiable boundary cases rather than reflecting systemic confusion.

The key insight is that the taxonomy definitions are clear, but **application requires understanding post intent and function, not just keyword matching**. Future iterations should include more explicit decision rules, additional edge case examples, and mandatory training exercises to calibrate annotators before independent work.

With the improvements suggested above, I expect future inter-annotator reliability would increase from 67.5% complete agreement to 80%+ complete agreement, making this taxonomy robust enough for larger-scale analysis of university subreddit content.