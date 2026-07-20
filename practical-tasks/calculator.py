"""
Build a Python calculator called calculator.py that takes two numbers as input and performs all four basic arithmetic operations plus two advanced operations. 
The calculator must handle user input safely using type casting and display results clearly using f-strings.
"""
# Prompt user input 
num1 = float(input("Enter num1: "))
num2 = float(input("Enter num2: "))

# Addition
addition = round(num1 + num2,2)
# Subtraction
subtraction = round(num1 - num2,2)
# Multiplication
multiplication = round(num1 * num2,2)
# Division
# Using ternary Operator
division = ("Division by zero not allowed, Try a different number!" if num2 == 0
      else round(num1 / num2,2))
# Floor Division
floor_division = ("Floor division by zero not allowed, Try a different number!" if num2 == 0
      else round(num1 // num2,2))
# Modulus
modulus = ("Modulus division by zero not allowed, Try a different number!" if num2 == 0
      else round(num1 % num2,2))

print(f"""
------------------------------------------
 Multi-function Calculator Table:
------------------+----------------------+
1. Addition       | (num1 + num2) = {addition}       
------------------+----------------------+
2. Subtraction    | (num1 - num2)  = {subtraction}    
------------------+----------------------+
3. Multiplication | (num1 * num2)  = {multiplication} 
------------------+----------------------+
4. Division       | (num1 / num2)  = {division}       
------------------+----------------------+
5. Floor-Division | (num1 // num2) = {floor_division} 
------------------+----------------------+
6. Modulus        | (num1 % num2)  = {modulus}        
------------------+----------------------+
""")



    

