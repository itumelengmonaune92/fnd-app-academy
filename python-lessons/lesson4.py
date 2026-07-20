# Basic control flow if/else statement scripts
age = int(input("Enter your age: "))
section_pass = input("Do you have a vip ticket? (yes/no) ").lower()

if age >= 18 and section_pass == "yes":
    print("Access granted to VIP section !!!")
elif age >= 18:
    print("Access granted to general section !!!")
else:
    print("Access denied !!!")