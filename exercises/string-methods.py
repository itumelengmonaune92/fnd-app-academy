
# Store a string object in a variable
course = "FNB App Academy!"
# Use the period to call all the methods/functions specific to the string datatype
upper_case = course.upper()
lower_case = course.lower()
title_format = course.title()
captial_letters = course.capitalize()
find_index = course.find("A")
replaced_string = course.replace("Academy", "Course")

# Display the output of showing how different methods affect the string
print()
print(f"1. Uppercase: {upper_case}")
print(f"2. Lowercase: {lower_case}")
print(f"3. Title: {title_format}")
print(f"4. Capitalize: {captial_letters}")
print(f"5. Character position: {find_index}")
print(f"6. Replaced string: {replaced_string}")
print("FNB" in course)
print("Itumeleng" in course)
print()