"""
Conditional statements and type conversion are used to build interactive programs 
that make decisions based on user input.

Write a simple weight converter program that asks the user for their weight 
and the unit of measurement, and then outputs the converted weight.

Conversion rules:
- If the weight is in Lbs ('l' or 'L'), convert it to Kg (Weight * 0.45)
- If the weight is in Kg ('k' or 'K'), convert it to Lbs (Weight / 0.45)

Your program should be case-insensitive to the unit input.

"""
attempts = 0
while attempts < 3:
    attempts += 1
    weight = int(input("Enter weight: "))
    conversion_unit = input("Unit of measurement (K)g or (L)bs: ")
   
    if conversion_unit.upper() == "L":
        weight *= 0.45
        print(f"Weight in Kg: {weight:.1f}")
    elif conversion_unit.upper() == "K":
        weight /= 0.45
        print(f"Weight in Lbs: {weight:.1f}")
    else:
        print("Invalid entry, enter a valid unit of measurement!")

