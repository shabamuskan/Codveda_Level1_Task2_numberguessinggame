import random

number = random.randint(1, 100)
attempts = 0
max_attempts = 7

print("Guess the number between 1 and 100. You have 7 tries.")

while attempts < max_attempts:
    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess == number:
        print("Congratulations! You guessed it right.")
        break
    elif guess < number:
        print("Too low!")
    else:
        print("Too high!")

if guess != number:
    print(f"Sorry, the correct number was {number}")
