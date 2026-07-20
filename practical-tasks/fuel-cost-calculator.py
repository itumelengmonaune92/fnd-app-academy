"""
The Challenge: "The South African Fuel Cost Calculator"

Background:
With petrol prices constantly shifting, drivers need a simple way to 
calculate their travel costs before hitting the road.

Requirements:
1. Input - Distance: 
   Prompt the user to enter the distance they plan to drive (in kilometers).
   
2. Input - Fuel Price: 
   Prompt the user for the current petrol price per liter (e.g., 22.45).
   
3. Calculation - Fuel Needed: 
   Calculate the total fuel required assuming the car consumes 1 liter 
   per 10 kilometers driven.
   Formula: liters_needed = kilometers / 10
   
4. Calculation - Total Cost: 
   Determine the total cost of the trip.
   Formula: total_cost = liters_needed * petrol_price
   
5. Data Handling & Formatting: 
   - Use type casting (`float()` / `int()`) to handle numerical user inputs safely.
   - Use `round()` to format the final total cost to 2 decimal places.
"""
# Request user for input data
kilometers = float(input("Enter distance(km): "))
petrol_price = float(input("Petrol price per litre (l): "))

litres_needed = kilometers / 10
total_cost = litres_needed * petrol_price

print(f"Your total cost to travel {kilometers}km is: R{round(total_cost, 2)} ")
