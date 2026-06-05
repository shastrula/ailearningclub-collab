# Part 4: Dictionaries

# Create a dictionary
student = {
    "name": "Alice",
    "age": 20,
    "major": "Computer Science",
    "gpa": 3.8
}

# Access values
print(student["name"])
print(student.get("email", "Not provided"))

# Loop through key-value pairs
for key, value in student.items():
    print(f"{key}: {value}")
