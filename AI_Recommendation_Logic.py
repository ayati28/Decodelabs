# Project 3: AI Recommendation Logic
# DecodeLabs - Artificial Intelligence

courses = {
    "Python Programming": ["python", "coding", "programming"],
    "Web Development": ["html", "css", "javascript", "web"],
    "Machine Learning": ["python", "ai", "machine learning"],
    "Data Science": ["python", "data", "analytics"],
    "Cloud Computing": ["cloud", "aws", "devops"],
    "Cyber Security": ["security", "networking", "hacking"],
    "Android Development": ["java", "android", "mobile"],
    "UI/UX Design": ["design", "figma", "creativity"]
}

print("=" * 50)
print("      AI RECOMMENDATION SYSTEM")
print("=" * 50)

user_input = input(
    "\nEnter your interests separated by commas:\n"
)

user_interests = [interest.strip().lower()
                  for interest in user_input.split(",")]

recommendations = []

for course, tags in courses.items():
    match_score = len(set(user_interests).intersection(set(tags)))

    if match_score > 0:
        percentage = (match_score / len(tags)) * 100
        recommendations.append((course, percentage))

recommendations.sort(key=lambda x: x[1], reverse=True)

print("\nRecommended Courses:\n")

if recommendations:
    for i, (course, percentage) in enumerate(recommendations[:3], start=1):
        print(f"{i}. {course} - {percentage:.0f}% Match")
else:
    print("No matching recommendations found.")

print("\nThank you for using the AI Recommendation System!")
