#!/usr/bin/env python3


import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter

# Actual posts from Concordia with final annotations
concordia_posts = [
    {"name": "t3_1ov92lh", "title": "You're all class traitors.", "you": "Social", "alex": "Student Governance", "jordan": "Social"},
    {"name": "t3_1ouuyls", "title": "STM STRIKE SUSPENDED?!", "you": "Campus Services", "alex": "Campus Services", "jordan": "Campus Services"},
    {"name": "t3_1ovdbyh", "title": "Student Housing - Survey", "you": "Housing", "alex": "Housing", "jordan": "Housing"},
    {"name": "t3_1otvjj6", "title": "Thoughts?", "you": "Social", "alex": "Social", "jordan": "Social"},
    {"name": "t3_1ov8y2j", "title": "Masters in public policy and administration MPPAA", "you": "Academic Planning", "alex": "Academic Planning", "jordan": "Academic Planning"},
    {"name": "t3_1ow4fl0", "title": "ENGR233 CLASS PROJECT ALEXANDRE PARADIS SECTION P", "you": "Course Content", "alex": "Course Content", "jordan": "Course Content"},
    {"name": "t3_1ouk1td", "title": "I need a tutor for ELEC 251 or I might end it", "you": "Academic Support", "alex": "Academic Support", "jordan": "Academic Support"},
    {"name": "t3_1otpd4u", "title": "Going backwards to retake classes", "you": "Academic Planning", "alex": "Academic Planning", "jordan": "Social"},
    {"name": "t3_1ovt5yo", "title": "Can conditional standing apply for graduation?", "you": "Academic Planning", "alex": "Academic Planning", "jordan": "Academic Planning"},
    {"name": "t3_1ouf0ad", "title": "How do I vote in the CSU elections?", "you": "Student Governance", "alex": "Student Governance", "jordan": "Student Governance"},
    {"name": "t3_1ow7lox", "title": "Comm 225 Final", "you": "Course Content", "alex": "Course Content", "jordan": "Course Content"},
    {"name": "t3_1oumbjx", "title": "Jan 2026 intake", "you": "Academic Planning", "alex": "Academic Planning", "jordan": "Academic Planning"},
    {"name": "t3_1ova59h", "title": "Question AFE bursary", "you": "Academic Planning", "alex": "Campus Services", "jordan": "Academic Planning"},
    {"name": "t3_1ovrmbi", "title": "Phys 204 final", "you": "Course Content", "alex": "Course Content", "jordan": "Course Content"},
    {"name": "t3_1otwzl4", "title": "SAE", "you": "Social", "alex": "Social", "jordan": "Academic Planning"},
    {"name": "t3_1ovq45c", "title": "There is no STM services for this weekend 15-16 November", "you": "Campus Services", "alex": "Campus Services", "jordan": "Campus Services"},
    {"name": "t3_1ovb6km", "title": "Room for rent this winter", "you": "Housing", "alex": "Housing", "jordan": "Housing"},
    {"name": "t3_1oves7y", "title": "Is Grey Nuns reading room incredibly cold?", "you": "Campus Services", "alex": "Campus Services", "jordan": "Social"},
    {"name": "t3_1ouj2y5", "title": "Are course evaluations reviewed?", "you": "Academic Planning", "alex": "Academic Planning", "jordan": "Academic Planning"},
    {"name": "t3_1ovfsxj", "title": "Med school from engineering", "you": "Academic Planning", "alex": "Academic Planning", "jordan": "Academic Planning"},
]

# Actual posts from McGill with final annotations
mcgill_posts = [
    {"name": "t3_1ovuvuc", "title": "PSYC337 midterm", "you": "Course Content", "alex": "Course Content", "jordan": "Course Content"},
    {"name": "t3_1osejkp", "title": "Language Poll", "you": "Social", "alex": "Social", "jordan": "Social"},
    {"name": "t3_1ourqiw", "title": "How to book a room in bronfman (3rd floor)", "you": "Campus Services", "alex": "Campus Services", "jordan": "Campus Services"},
    {"name": "t3_1our5li", "title": "Some of you guys can't stop vomiting words for 50 mins", "you": "Social", "alex": "Social", "jordan": "Social"},
    {"name": "t3_1oq5y98", "title": "Best pizza place near campus", "you": "Social", "alex": "Campus Services", "jordan": "Social"},
    {"name": "t3_1opld6e", "title": "ECON230 midterm", "you": "Course Content", "alex": "Course Content", "jordan": "Course Content"},
    {"name": "t3_1os2tp9", "title": "McGill Speedcube Club is here!", "you": "Social", "alex": "Social", "jordan": "Social"},
    {"name": "t3_1oq1nky", "title": "Closest covered bike rack near SSMU centre", "you": "Campus Services", "alex": "Campus Services", "jordan": "Campus Services"},
    {"name": "t3_1oqjf2j", "title": "Prof inputted wrong grade on my courses", "you": "Academic Planning", "alex": "Course Content", "jordan": "Academic Planning"},
    {"name": "t3_1or0qy3", "title": "Best pizza place in campus", "you": "Social", "alex": "Campus Services", "jordan": "Social"},
    {"name": "t3_1orytj7", "title": "Is there an Electrical Enginering Helpline community", "you": "Academic Support", "alex": "Academic Support", "jordan": "Campus Services"},
    {"name": "t3_1otg9do", "title": "McGill University MRI study recruiting people with and without Long COVID", "you": "Employment", "alex": "Employment", "jordan": "Employment"},
    {"name": "t3_1op86kx", "title": "ECON 313 second midterm?", "you": "Course Content", "alex": "Course Content", "jordan": "Course Content"},
    {"name": "t3_1ovdfvl", "title": "Introduction to Quantitative Political Science. - POLI 311 with Aaron Erlich", "you": "Course Content", "alex": "Course Content", "jordan": "Academic Planning"},
    {"name": "t3_1ouyv3v", "title": "Gym at McGill", "you": "Campus Services", "alex": "Campus Services", "jordan": "Campus Services"},
    {"name": "t3_1ovcwss", "title": "Math Minor worth it?", "you": "Academic Planning", "alex": "Academic Planning", "jordan": "Social"},
    {"name": "t3_1ow40z9", "title": "Where do people print stickers around here?", "you": "Campus Services", "alex": "Campus Services", "jordan": "Social"},
    {"name": "t3_1or0jgt", "title": "life if i never got another ssmu email ever again", "you": "Social", "alex": "Social", "jordan": "Student Governance"},
    {"name": "t3_1oul8c3", "title": "PDF of your degree", "you": "Academic Planning", "alex": "Academic Planning", "jordan": "Campus Services"},
    {"name": "t3_1ot0j2y", "title": "I Failed my biol 200 midterm", "you": "Course Content", "alex": "Course Content", "jordan": "Academic Support"},
]

def compute_agreement(posts):
    """Compute agreement statistics for annotated posts."""
    complete_agreement = []
    majority_agreement = []
    no_agreement = []
    
    for post in posts:
        annotations = [post["you"], post["alex"], post["jordan"]]
        counts = Counter(annotations)
        most_common = counts.most_common(1)[0]
        
        if most_common[1] == 3:  # All 3 agree
            complete_agreement.append(post)
        elif most_common[1] == 2:  # 2 out of 3 agree
            majority_agreement.append(post)
        else:  # All different
            no_agreement.append(post)
    
    return complete_agreement, majority_agreement, no_agreement

def create_final_dataset(posts):
    """Create final labeled dataset using majority vote + arbitration."""
    final_posts = []
    
    for post in posts:
        annotations = [post["you"], post["alex"], post["jordan"]]
        counts = Counter(annotations)
        most_common = counts.most_common(1)[0]
        
        if most_common[1] >= 2:  # Majority exists
            final_label = most_common[0]
        else:  # No majority - you act as arbitrator
            final_label = post["you"]  # Use your judgment as tiebreaker
        
        final_posts.append({
            "Name": post["name"],
            "title": post["title"],
            "coding": final_label
        })
    
    return final_posts

# Task 7: Compute agreement
print("=" * 70)
print("TASK 7: ANNOTATOR AGREEMENT ANALYSIS")
print("=" * 70)

print("\n--- McGill Posts ---")
mcgill_complete, mcgill_majority, mcgill_no = compute_agreement(mcgill_posts)
print(f"Complete agreement (3/3): {len(mcgill_complete)} posts ({len(mcgill_complete)/len(mcgill_posts)*100:.1f}%)")
print(f"Majority agreement (2/3): {len(mcgill_majority)} posts ({len(mcgill_majority)/len(mcgill_posts)*100:.1f}%)")
print(f"No agreement (0/3): {len(mcgill_no)} posts ({len(mcgill_no)/len(mcgill_posts)*100:.1f}%)")
print(f"\nTotal with at least majority: {len(mcgill_complete) + len(mcgill_majority)} / {len(mcgill_posts)} ({(len(mcgill_complete) + len(mcgill_majority))/len(mcgill_posts)*100:.1f}%)")

print("\n--- Concordia Posts ---")
concordia_complete, concordia_majority, concordia_no = compute_agreement(concordia_posts)
print(f"Complete agreement (3/3): {len(concordia_complete)} posts ({len(concordia_complete)/len(concordia_posts)*100:.1f}%)")
print(f"Majority agreement (2/3): {len(concordia_majority)} posts ({len(concordia_majority)/len(concordia_posts)*100:.1f}%)")
print(f"No agreement (0/3): {len(concordia_no)} posts ({len(concordia_no)/len(concordia_posts)*100:.1f}%)")
print(f"\nTotal with at least majority: {len(concordia_complete) + len(concordia_majority)} / {len(concordia_posts)} ({(len(concordia_complete) + len(concordia_majority))/len(concordia_posts)*100:.1f}%)")

# Task 8: Identify disagreements
print("\n" + "=" * 70)
print("TASK 8: DISAGREEMENT ANALYSIS")
print("=" * 70)

all_disagreements = mcgill_majority + mcgill_no + concordia_majority + concordia_no

print(f"\nTotal posts with any disagreement: {len(all_disagreements)} / 40 ({len(all_disagreements)/40*100:.1f}%)")
print("\nDetailed breakdown of disagreements:\n")

for i, post in enumerate(all_disagreements, 1):
    annotations = [post["you"], post["alex"], post["jordan"]]
    counts = Counter(annotations)
    if counts.most_common(1)[0][1] == 1:
        agreement_type = "NO AGREEMENT"
    else:
        agreement_type = "MAJORITY"
    
    print(f"{i}. [{agreement_type}] \"{post['title']}\"")
    print(f"   You: {post['you']:20s} | Alex: {post['alex']:20s} | Jordan: {post['jordan']:20s}")
    print()

# Task 9: Create final datasets
print("=" * 70)
print("TASK 9: CREATING FINAL LABELED DATASETS")
print("=" * 70)

mcgill_final = create_final_dataset(mcgill_posts)
concordia_final = create_final_dataset(concordia_posts)

# Save to TSV
mcgill_df = pd.DataFrame(mcgill_final)
concordia_df = pd.DataFrame(concordia_final)

mcgill_df.to_csv('final_labeled_dataset_mcgill.tsv', sep='\t', index=False)
concordia_df.to_csv('final_labeled_dataset_concordia.tsv', sep='\t', index=False)

print("\n✓ Created: final_labeled_dataset_mcgill.tsv")
print("✓ Created: final_labeled_dataset_concordia.tsv")
print(f"\nFinal datasets contain {len(mcgill_final)} McGill posts and {len(concordia_final)} Concordia posts")

# Task 10: Plot results
print("\n" + "=" * 70)
print("TASK 10: VISUALIZING RESULTS")
print("=" * 70)

# Count categories
mcgill_counts = Counter([p['coding'] for p in mcgill_final])
concordia_counts = Counter([p['coding'] for p in concordia_final])

# Get all categories in order
all_categories = ['Academic Planning', 'Academic Support', 'Campus Services', 
                  'Course Content', 'Employment', 'Housing', 'Social', 'Student Governance']

# Filter to only categories that appear in our data
categories_in_data = [cat for cat in all_categories 
                      if mcgill_counts.get(cat, 0) > 0 or concordia_counts.get(cat, 0) > 0]

# Prepare data for plotting
mcgill_values = [mcgill_counts.get(cat, 0) for cat in categories_in_data]
concordia_values = [concordia_counts.get(cat, 0) for cat in categories_in_data]

# Create bar chart
fig, ax = plt.subplots(figsize=(14, 7))
x = range(len(categories_in_data))
width = 0.35

bars1 = ax.bar([i - width/2 for i in x], mcgill_values, width, 
               label='McGill', color='#ED1B2F', alpha=0.8)
bars2 = ax.bar([i + width/2 for i in x], concordia_values, width, 
               label='Concordia', color='#912338', alpha=0.8)

# Add value labels on bars
for bars in [bars1, bars2]:
    for bar in bars:
        height = bar.get_height()
        if height > 0:
            ax.text(bar.get_x() + bar.get_width()/2., height,
                   f'{int(height)}',
                   ha='center', va='bottom', fontsize=10, fontweight='bold')

ax.set_xlabel('Category', fontsize=13, fontweight='bold')
ax.set_ylabel('Number of Posts', fontsize=13, fontweight='bold')
ax.set_title('Topic Distribution: r/mcgill vs r/concordia\n(Sample of 20 posts per subreddit)', 
             fontsize=15, fontweight='bold', pad=20)
ax.set_xticks(x)
ax.set_xticklabels(categories_in_data, rotation=45, ha='right', fontsize=11)
ax.legend(fontsize=12, loc='upper right')
ax.grid(axis='y', alpha=0.3, linestyle='--')
ax.set_ylim(0, max(max(mcgill_values), max(concordia_values)) + 2)

plt.tight_layout()
plt.savefig('results.png', dpi=300, bbox_inches='tight')
print("\n✓ Created: results.png")

print("\n--- Category Distribution ---")
print("\nMcGill:")
for cat in categories_in_data:
    count = mcgill_counts.get(cat, 0)
    pct = count / len(mcgill_final) * 100
    print(f"  {cat:25s}: {count:2d} posts ({pct:5.1f}%)")

print("\nConcordia:")
for cat in categories_in_data:
    count = concordia_counts.get(cat, 0)
    pct = count / len(concordia_final) * 100
    print(f"  {cat:25s}: {count:2d} posts ({pct:5.1f}%)")

# Key observations
print("\n" + "=" * 70)
print("KEY OBSERVATIONS")
print("=" * 70)

print("\nDifferences between subreddits:")
for cat in categories_in_data:
    m_count = mcgill_counts.get(cat, 0)
    c_count = concordia_counts.get(cat, 0)
    if m_count != c_count:
        diff = m_count - c_count
        if diff > 0:
            print(f"  • McGill has {diff} more {cat} post(s)")
        else:
            print(f"  • Concordia has {-diff} more {cat} post(s)")

print("\nMost common topics:")
print(f"  • McGill: {mcgill_counts.most_common(1)[0][0]} ({mcgill_counts.most_common(1)[0][1]} posts)")
print(f"  • Concordia: {concordia_counts.most_common(1)[0][0]} ({concordia_counts.most_common(1)[0][1]} posts)")

print("\n" + "=" * 70)
print("ANALYSIS COMPLETE!")
print("=" * 70)
print("\nGenerated files:")
print("  ✓ final_labeled_dataset_mcgill.tsv")
print("  ✓ final_labeled_dataset_concordia.tsv")
print("  ✓ results.png")
print("\nNext step: Review error_assessment.md for detailed disagreement analysis")