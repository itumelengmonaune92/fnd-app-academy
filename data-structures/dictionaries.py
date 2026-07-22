# Dictionaries Hashmaps/Associative Arrays
# Keys and values can be of any datatype
# Looking for a key that does not exits throws a KeyError us .get() to avoid error and rather return None
student = {'name': 'Itumeleng', 'age': 25, 'courses': ['Maths', 'CompSci']}

# new key-pair to our student
student['phone'] = '0680955507'
# Update exiting key-pair and and new key-pair at the same time
student.update({'name': 'Vincent', 'age': 34, 'phone': '0783742114'})

# delete course from the dictionary
del student['courses'] # or use pop removed_course = student.pop('course')
print()
print(f"1. Updated dictionary: {student}")
print(f"2. The dictionary contains '{len(student)}' key-value pairs")
print(f"3. The dictionary contains the following keys: {student.keys()}")
print(f"4. The dictionary contains the following values: {student.values()}")
print(f"5. The dictionary contains the following key-values pairs: {student.items()}")

# Use a for loop to print each key and its values
print()
print("Student Information:")
for key, value in student.items():
    print(f"* {key.title()}: {value}")
print()


