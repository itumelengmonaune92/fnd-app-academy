"""
Python lists are ordered, mutable collections of items. They allow you to store, 
access, modify, and analyze sequences of data dynamically.

Write a program that acts as a basic inventory management system for a fantasy RPG game. 
Your program should perform the following operations using a list of inventory items:

1. Start with an inventory list containing exactly these five starting items: 
   "iron sword", "leather shield", "wooden staff", "healing potion", and "mana potion".

2. Print the first and the last items in the inventory using indexing.

3. The player finds a treasure chest! Add a new item, "golden chalice", to the 
   end of the inventory list.

4. The player uses their healing potion. Find the position (index) of "healing potion" 
   in the list, and remove it from the inventory.

5. The player upgrades their shield. Replace "leather shield" with "steel shield" 
   at its current position.

6. Print the player's final inventory, sorted alphabetically, alongside the total 
   number of items they are currently carrying.

"""

# Question 1
inventory = ["iron sword", "leather shield", "wooden staff", "healing potion", "mana potion"]

# Question 2
print()
print(f"First item: {inventory[0]}\nLast item: {inventory[-1]}")
print()

# Question 3
inventory.append("golden chalice")
print(f"New item added: {inventory}")
print()

# Question 4
potion_index = inventory.index('healing potion')
inventory.pop(potion_index)
print(f"Item {potion_index} has been removed from the inventory")
print()

# Question 5
inventory[1] = "steel shield"
print(f"Updated list: {inventory}")
print()

# Question 6
inventory.sort()
print(f"Sorted list: {inventory}\nTotal item: {len(inventory)}")