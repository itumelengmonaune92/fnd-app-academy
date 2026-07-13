# Store two values in separate variablse as integers and output the sum of both
num1 = int(input("Enter any number from (1-9): "))
num2 = float(input("Enter any number from (0.0-0.9): "))

# Use the addition operator to generate the sum of both values
print(f"1. The toal sum of {num1} and {num2} using the addition operator is: {num1 + num2}")
# Generate the sum of both num1 and num2 using the built-in sum function
# Note: the sum function only works on iterables. wrap the two numbers in square brackest to convert them into a list.
print(f"2. The toal sum of {num1} and {num2} using the sum function is: {sum([num1, num2])}")