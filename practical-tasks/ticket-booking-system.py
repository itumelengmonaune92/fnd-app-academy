"""
Create a program that acts as a digital ticket counter.
"""

# Collect user information
name = input("Enter your name: ")
artist_band = input("Which artist/band are you here to see: ")
confirmation_message = (f"Hey {name.title()}! Your tickets to see {artist_band.title()} are booked successfully!")

# Display custom ticket confirmation message
print()
print(confirmation_message)
print()