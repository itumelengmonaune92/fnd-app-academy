"""
======================================================================
TASK 1: The "Real-World Policy" Translate
======================================================================
SCENARIO:
You are writing the safety logic for a theme park roller coaster. 
The park has the following strict rules for riders:
1. A person must be at least 48 inches tall to ride alone.
2. If they are accompanied by an adult, they can ride if they are 
   at least 42 inches tall.
3. In all cases, anyone over 80 inches tall is too tall to ride.

YOUR GOAL:
1. Create variables for a rider: `height` (an integer) and 
   `with_adult` (a boolean).
2. Write a single compound Python expression (using comparison and 
   logical operators) that evaluates to True if they are allowed 
   to ride, and False if they are not.
3. Assign this expression to a variable named `can_ride`.
4. Test it with different inputs (e.g., height=45, with_adult=True).
"""

# Using if statements
# Top to bottom (Sequencial Control Flow)
height = int(input("Enter height: "))
with_adult = input(("Are you with an adult: (yes/no)? ")).strip().lower()

if height >= 48:
    print(True)
elif height >= 42 and with_adult == "yes":
    print(True)
elif height >= 42 and with_adult == "no":
    print(False)
elif height < 42:
    print(False)
else:
    print(True)

# Use boolean expression
# Inside out (Travesal)
can_ride = height <= 80 and (height >= 48 or (height >=42 and with_adult == "yes"))
print(can_ride)