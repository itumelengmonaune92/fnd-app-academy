"""
Secure Password Hint Generator

Instructions for the script:
1. Prompt the user to input their secret password.
2. Clean up any accidental leading or trailing whitespace using the .strip() method.
3. Extract the first and last characters of the cleaned password using string indexing.
4. Display a secure hint using an f-string, ensuring the extracted first and last 
   letters are converted to uppercase for visibility.
   
Example Output Format:
"Your password hint: It starts with [FIRST_LETTER] and ends with [LAST_LETTER]"
"""

password = input("Enter your secret password: ")
password.strip()

first_character = password[0]
last_character = password[-1]

password_hint = f"Your password hint: It starts with {first_character.upper()} and ends with {last_character.upper()}."
print(password_hint)