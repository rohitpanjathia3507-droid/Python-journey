# day6_guessing_game.py
import random
number = random.randint(1, 100)
name = input("Enter your name: ")
guess = int(input("Enter your guess: "))
attempt = 1
while (guess != number):
    if (guess < number):
        print("Too low")
    elif (guess > number):
        print("Too high")
    guess = int(input("Enter your guess: "))
    attempt += 1
print(f"Congratulations {name}! You guessed the right number in {attempt} attempts")