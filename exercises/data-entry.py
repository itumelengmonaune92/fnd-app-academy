#Checking-in a new patient at a hospital.

patients = ["Thabo", "Itumeleng", "Lerato"]

name = input("Enter your name: ")
age = input("How old are you: ")
is_patient = True

if name in patients:
    print(f"{name}, age {age}, patient status={is_patient}.\n{name} is an exsiting patient")
else:
    print(f"{name}, age {age}, patient status={not is_patient}.\nNo records were found, create a new profile for {name}")
   