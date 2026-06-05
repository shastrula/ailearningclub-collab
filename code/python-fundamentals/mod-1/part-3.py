# Part 3: Lists & Loops

# Create a list
languages = ["Python", "JavaScript", "Java", "C++"]
print(f"Total languages: {len(languages)}")

# Loop through items
for lang in languages:
    print(f"Learning: {lang}")

# Add and remove
languages.append("Go")
languages.remove("Java")
print(languages)
