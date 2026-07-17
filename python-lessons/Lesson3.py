# Manipulating numbers
# adding two numbers
num1 = input("Enter the first number: ")
num2 = input("Enter the first number: ")

# Print the sum of both number without type-casting
print("\nPrint the sum of both number without type casting")
result1 = num1 + num2
print(f"1. The sum of num1 and num2 without type casting is: {result1} of type -> ({type(result1)}).\n") # the result is string concatenation

# Print the sum of both number using type-casting
print("Print the sum of both number using type-casting")
result2 = int(num1) + int(num2)
print(f"2. The sum of num1 and num2 using type-asting is: {result2} of type -> ({type(result1)}).\n") # the result is string concatenation

