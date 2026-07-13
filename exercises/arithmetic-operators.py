num1 = int(input("Enter num1: "))
num2 = int(input("Enter num2: "))

addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
exponent = num1 ** num2

division = num1 / num2
# Rounds down to the lowest whole integer
floor_division = num1 // num2
# Return the remainder
modulus = num1 % num2

# Display the output results for each arithmetic operator
print()
print(f"1. Addition Operator: {addition}")
print(f"2. Subtraction Operator: {subtraction}")
print(f"3. Multiplication Operator: {multiplication}")
print(f"4. Division Operator: {division:.2}")
print(f"5. Floor Division Operator: {floor_division}")
print(f"6. Modulus Operator: {modulus}")
print(f"7. Exponent Operator: {exponent}")
print()


