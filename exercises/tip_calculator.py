# Build a small script that helps calculate tips at a resturant
bill = float(input("Enter the bill: R"))
tip = 0.15 # Written in decimal

tip_value = bill * tip
total_cost = bill + tip_value

# print the total tip value
print()
print("Print the total tip value")
print(f"The total value of the tip is: {tip_value}")
print(f"The total value of the tip rounded is: {round(tip_value,2)}\n")

# print the total tip value
print("Print the total cost of the bill")
print(f"The total bill value is: {total_cost}")
print(f"The total bill value rounded is: {round(total_cost,2)}\n")