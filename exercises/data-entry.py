#Checking-in a new patient at a hospital.

patients = ["Thabo", "Itumeleng", "Lerato"]

#All user inputs return "str" values
name = input("Enter your name: ")
# Convert birth_year value to integer
birth_year = int(input("Which year were you born: "))
age = 2026 - birth_year
is_patient = True

if name in patients:
    print(f"{name}, age {age}, patient status={is_patient}.\n{name} is an exsiting patient")
else:
    print(f"{name}, age {age}, patient status={not is_patient}.\nNo records were found, create a new profile for {name}")
   