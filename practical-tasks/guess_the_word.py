# Design a guessing gaming using loops
secret_word = "python"
print()
print("Welcome to Guess the word.")
while True:
    guess = input("1. Guess the programming language we are using: ").lower()
    if guess == secret_word:
        print("Congratulations, you guessed the correct language!")
        break
    else:
        print("Incorrect guess, try again!")

