# Generate numbers from 1 to 10 using the range function
# Stored in a variable using list comprehension
numbers = list(range(11)) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Print all number on a new line using a for Loop
print("Print all number on a new line using a for loop")
for number in numbers:
    print(number)

# Print all number on a new line using a while Loop
print()
print("Print all number on a new line using a while loop")
i = 0
while i < len(numbers):
    print(numbers[i])
    i += 1
