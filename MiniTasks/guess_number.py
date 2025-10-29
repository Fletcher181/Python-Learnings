import random as rd

secret_number = rd.randint(1, 10)
print("Welcome to number guessing game.")

while True:
    guess_number = int(input("\nPick a number between 1 and 10: "))

    if guess_number < 1 or guess_number > 10 or guess_number:
        print("Please input a valid number!")
        continue
    if guess_number == secret_number:
        print("You guessed the number correctly!")
        break
    elif guess_number > secret_number:
        print("Guess again. Hint: Guess Lower.")
    elif guess_number < secret_number:
        print("Guess again. Hint: Guess Higher.")