# University Subreddit Post Taxonomy Guide

**Author:** Kanika Singh Pundir 
**Date:** November 19, 2025  
**Subreddits:** r/mcgill and r/concordia  
**Sample Size:** 100 posts (50 per subreddit)

---

## 1. Motivation

I built this taxonomy to understand what students at McGill and Concordia actually talk about on their subreddits. By categorizing posts, I wanted to see if there are patterns in what students care about and whether the two communities discuss different things.

This matters because these subreddits are where students go for real-time help, advice, and community. Understanding the main topics can reveal what students prioritize, what problems they face, and how they use online spaces to navigate university life. The taxonomy gives us a way to count and compare these patterns systematically.

I designed this coding scheme so that anyone could pick it up and classify posts consistently, which makes it possible to analyze larger datasets or compare across different university communities.

---

## 2. Taxonomy Categories

### 2.1 Course Content
**Definition:** Posts asking about or discussing specific coursework, exams, assignments, or grades. The key here is that the post mentions a specific course code (like COMP 352 or BIOL 111) and is focused on the actual content or assessment in that course.

**Examples (What's In):**
- "COMP 352 midterm grades + what's considered a Passing Letter grade for this course?" – wants to know about grading in this specific course
- "Failed biol 111 midterm" – sharing exam results
- "comm309 and acco310 final" – asking about finals in these courses
- "ELEC 372 midterm" – course-specific exam question

**Edge Cases:**
- *IN:* "COMP 421 to learn SQL?" – Even though this sounds like course selection, it's really asking what specific content this course covers, so it goes here
- *IN:* "CALLING ALL THOSE WHO TOOK PHGY 209" – Looking for people who can share info about this specific course
- *OUT:* "How do you study for ECON 201/203 final" → **Academic Support** – This is about study strategies, not the course content itself. The focus is HOW to study, not WHAT is on the exam
- *OUT:* "Need Tutor for ELEC 273" → **Academic Support** – Looking for help, not discussing course material

---

### 2.2 Academic Planning
**Definition:** Posts about navigating university systems and making academic decisions. This includes choosing programs, selecting courses, dealing with administrative stuff, transfers, and planning your academic path. Basically, it's about figuring out the system, not learning the material.

**Examples (What's In):**
- "Med school from engineering" – planning a major academic transition
- "Question abt transferring to JMSB" – navigating the transfer process
- "what are some electives I should take if i'm into screenwriting but not a film student?" – getting advice on course selection
- "Messed up my transcripts and lost on what to do now" – dealing with an administrative problem
- "double major experiences advice?" – deciding whether to do a double major

**Edge Cases:**
- *IN:* "GPA 2.70" – This is probably about what having a 2.70 GPA means for their academic standing or future, not about a specific course
- *IN:* "Are course evaluations reviewed?" – Asking about an administrative process
- *OUT:* "COMP 352 midterm grades" → **Course Content** – This is about performance in a specific course
- *OUT:* "Need Tutor for ELEC 273" → **Academic Support** – Looking for learning help, not navigating the system

---

### 2.3 Academic Support
**Definition:** Posts where someone is seeking or offering help with learning. This includes requests for tutors, questions about study strategies, posts about struggling with material, or asking for general academic advice. The focus is on "help me learn" rather than "help me navigate the system."

**Examples (What's In):**
- "Need Tutor for ELEC 273" – looking for a tutor
- "comm 205 how to study for final" – wants study tips
- "How do you study for ECON 201/203 final" – asking for study strategies
- "Struggling with Discrete Math [COEN 231]" – having trouble with the material
- "interested in bioinformatics, but struggling with courses in comp minor" – finding courses difficult

**Edge Cases:**
- *IN:* "Struggling with chronic pain as a McGill student" – Even though this mentions health, the focus is on how it affects their academics
- *IN:* "Is there an Electrical Engineering Helpline community" – Looking for academic support resources
- *OUT:* "COMP 352 midterm grades" → **Course Content** – Asking about grades, not seeking help
- *OUT:* "Should I drop out?" → **Academic Planning** – This is a big decision about navigating their academic path

---

### 2.4 Student Governance
**Definition:** Posts about official student government stuff like CSU or SSMU, including elections, statements from student unions, or student government activities. This is specifically about the political/organizational side of student life.

**Examples (What's In):**
- "The CSU prepares for a by-election despite low student engagement" – student union election news
- "How do I vote in the CSU elections?" – asking about the voting process
- "CSU statement on STM strike" – official statement from student government
- "I hope everyone who upvoted this actually opens their email and votes in the by-election" – encouraging election participation

**Edge Cases:**
- *IN:* Anything about official student union positions, policies, or activities
- *OUT:* "Mice in SSMU Building" → **Campus Services** – Even though SSMU is the student union building, this is about a facility problem, not governance
- *OUT:* "McGill Speedcube Club is here!" → **Social** – This is a student club, not student government
- *OUT:* "STM STRIKE SUSPENDED?!" → **Campus Services** – This is about public transit, not student government

---

### 2.5 Campus Services
**Definition:** Posts about campus facilities, transportation, buildings, and services. This includes stuff like gyms, libraries, food places, building access, transit (including STM since it affects getting to campus), and campus technology. Basically, the infrastructure and services that make campus work.

**Examples (What's In):**
- "Is transit back?" – asking about transportation
- "STM STRIKE SUSPENDED?!" – transit affecting campus access
- "lockers" – asking about campus lockers
- "PSA: Theft at McGill Gym Lockers" – campus facility safety warning
- "How to book a room in bronfman (3rd floor)" – how to use a campus facility
- "Where do people print stickers around here?" – looking for a campus service

**Edge Cases:**
- *IN:* "Greenshield health insurance access" – This is a service the university provides
- *IN:* "Avoid front gates if you don't have waterproof boots" – Practical info about campus infrastructure
- *OUT:* "Room for rent this winter" → **Housing** – This is about off-campus housing
- *OUT:* "How do I vote in the CSU elections?" → **Student Governance** – About elections, not services
- *OUT:* "Best pizza place in campus" → **Social** – This is more of a casual recommendation than a service question

---

### 2.6 Housing
**Definition:** Posts about finding a place to live, including room rentals, roommate searches, housing surveys, or issues with leases and residence life.

**Examples (What's In):**
- "Room for rent this winter" – advertising a room for rent
- "Student Housing - Survey" – survey about housing

**Edge Cases:**
- *IN:* Posts about sublets, lease problems, or residence contracts
- *OUT:* If someone is asking about residence buildings but it's focused on facilities (like "Is there a gym in rez?") → **Campus Services**
- *OUT:* "Mice in SSMU Building" → **Campus Services** – This is a building facility issue, not housing

---

### 2.7 Employment
**Definition:** Posts about jobs, work opportunities, TA/RA positions, internships, career-building volunteer gigs, or anything related to getting paid work. This also includes paid research studies since participants are compensated.

**Examples (What's In):**
- "Does anyone know about a job?" – job hunting
- "TA Hiring Application System - inquiry" – asking about TA positions
- "VOLUNTEER OPPORTUNITY - INTERNATIONAL CASE COMPETITION 2026" – career-building opportunity
- "Recruiting participants for paid study!" – paid research participation
- "Staff benefits" – question about employment benefits

**Edge Cases:**
- *IN:* Paid research participation counts here because there's compensation
- *OUT:* "Contacting supervisors for MA" → **Academic Planning** – This is about applying to grad school, not getting a job
- *OUT:* If someone is looking for an unpaid study buddy or collaboration → **Academic Support**

---

### 2.8 Social
**Definition:** The catch-all category for everything else. This includes social activities, gaming, campus culture posts, clubs (that aren't student government), lost & found, casual conversations, memes, personal thoughts, or anything that's just people chatting and building community.

**Examples (What's In):**
- "Anyone wants to play ARC Raiders?" – looking for gaming buddies
- "Lost AirpodsPro found in EV building" – lost and found
- "counting the days until this fuckass semester ends" – venting/personal expression
- "Do you study on Friday night?" – casual social question
- "Best pizza place in campus" – casual recommendation request
- "McGill Speedcube Club is here!" – student club announcement
- "Thoughts?" – super vague, probably just starting a conversation

**Edge Cases:**
- *IN:* "Some of you guys can't stop vomiting words for 50 mins" – Commenting on social behavior, clearly social
- *IN:* "Can I use the bathroom - comp 206" – Even though it mentions a course, this feels like a joke or casual comment
- *IN:* "What would make the STM fare system better in your opinion?" – This is opinion/discussion, not an immediate service problem
- *IN:* "FREE - molecular chemistry kit - pick up @ du Parc/Milton" – Community exchange/giveaway
- *OUT:* "COMP 352 midterm grades" → **Course Content** – This is genuinely about academics
- *OUT:* "Is transit back?" → **Campus Services** – Asking for real info about a service

---

## 3. How the Categories Work Together

The eight categories are designed to be mutually exclusive (each post goes in exactly one category) and comprehensive (every post fits somewhere). Here's how I think about them:

**The Academic Trio** (Course Content, Academic Planning, Academic Support) all deal with academics but in different ways:
- **Course Content** = "What's in this course?"
- **Academic Planning** = "How do I navigate the university system?"
- **Academic Support** = "Help me learn this material"

**Campus Life Categories** (Student Governance, Campus Services, Housing, Employment) are separated by domain:
- **Student Governance** = official student unions and politics
- **Campus Services** = facilities and infrastructure
- **Housing** = where you live
- **Employment** = how you make money

**Social** is the catch-all for everything else, especially community-building and casual interactions.

When I tested this on 100 posts, every single one fit into exactly one category. The trickiest calls were usually between Course Content and Academic Support (solved by asking "is this about the material or about getting help?") and between Campus Services and Social (solved by asking "is this a real service question or just casual chat?").

**My rule of thumb:** When a post could fit multiple categories, I go with whatever the main point seems to be. What is the person actually trying to accomplish with this post? That usually makes it pretty clear.