# Tracking individual letters
name = "Itumeleng"

# In python counting starts from position the value 0
print()
print("Print individual string characters at thier specific positions")
print(f"1. Letter at position 1: {name[0]}")
print(f"2. Letter at position 2: {name[2]}")
print(f"3. Letter at the last position: {name[-1]}")
print()

# Using String methods
print("Using String methods")
course = "   Python   "
print(f"String in capital letters: {course.upper()}")
print(f"String with no trailing spaces: {course.strip()}")
print()

# Task: Create aprofessional email generating system
print("Task: Create aprofessional email generating system")
first_name = input("Enter your first name: ").strip()
last_name = input("Enter your last name: ").strip()
domain = "@fnbacademy.com"

username = f"{first_name[0:2]}{last_name}"
print(f"Your username is: {username.lower()}{domain.lower()}")
print()
