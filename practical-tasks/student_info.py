"""
Write a script to collect personal information from user.
Display user information in a formatted card.

Variables:
first_name (str)
last_name (str)
age (int)
favourite_num (float)

"""
# Collect first name, surname, age (as int) and favourite number (as float)
first_name = input("Enter your first name: ")
surname = input("Enter your surnname: ")
age = int(input("How old are you?: "))
favourite_num = float(input("What is your favourite number: "))

# Display the profile card welcome message
print()
print("=" * 45)
print(f"{' '* 8} Welcome, {(first_name + ' ' + surname).upper().title()}!")
print("=" * 45)

# Display student's age in months and favourite number rounded to two decimal places
print(f"Age:{' '* 17} {age} months old")
print(f"Favourite number: {' '* 3} {round((favourite_num),2)}")
print("=" * 45)
print()

# Print the data type of each collected value
print(f"Firstname datatype:{' '* 11} {type(first_name)}")
print(f"Surname datatype:{' '* 13} {type(surname)}")
print(f"Age datatype:{' '* 17} {type(age)}")
print(f"Favorite number datatype:{' '* 5} {type(favourite_num)}")
print("=" * 45)
print()

name = "Itumeleng"



