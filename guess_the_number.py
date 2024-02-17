from logo import logo
import random

number = random.randint(1, 100)
print(logo)
print("Welcome to the Number Guessing Game!")
print("I am thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty. Type 'easy', 'medium' or 'hard': ")

if difficulty == "hard":
    attempts = 5
elif difficulty == "medium":
    attempts = 7
else:  # If the player can't follow basic directions such as typing a word that is in front of him
    # the difficulty is automatically set to easy
    attempts = 10

guess = 0
while guess != number:
    print(f"You have {attempts} attempts remaining to guess the number")
    player_input = input("Make a guess: ")
    if not player_input.isdigit():
        print("Invalid input. Try again...")
        continue
    guess = int(player_input)
    if guess > number:
        print("Too high")
        print("Guess again.")
        attempts -= 1
    elif guess < number:
        print("Too low")
        print("Guess again.")
        attempts -= 1

    if attempts < 1:
        break

if guess == number:
    print(f"You got it! The answer was {number}.")
else:
    print(f"You have run out of guesses, you lose. The answer was {number}.")


