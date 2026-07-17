"""
Write a Python script called string_formatter.py that takes a user’s first name, 
last name, and a short bio message as input, then applies multiple string transformations 
to produce a formatted user profile output. This simulates how a real app backend processes user-submitted text.

"""

first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
bio_message = input("Provide a short professiona bio about yourself: ")

# Apply multiple string transformation to all the data provided by user
print()
username = f"{first_name[0]}{last_name}"
print(f"User name: {username.lower()}")

full_name = f"{first_name} {last_name}"
print(f"Full name: {full_name.title()}")

stripped_bio = bio_message.strip()
print(f"Professional Summary: {stripped_bio}")
print(f"Numer of characters in bio: {len(stripped_bio)}")

# Replace any occurrence of ‘I am’ in the bio with ‘I’m’ using .replace()
new_bio = stripped_bio.replace("I am", "I'm")
print(f"New professional Summary: {new_bio}")
print()
print("Display all output using f-strings")
print(f"User name: {username.lower()}\nFull name: {full_name.title()}\nProfessional Summary: {bio_message.strip()}\nNumer of characters in bio: {len(bio_message)}\nNew professional Summary: {new_bio}")
# I am a Full Stack Software Engineer.