# Python number Guessing Game
import random

lowest_num = 10
highest_num = 100
answer = random.randint(lowest_num, highest_num)
guesses = 0
is_running = True

print("python Number Guessing Game")
print(f"Select a number between {lowest_num} and {highest_num}")
while is_running:
    guesses = input("Enter your guess:")
    if guesses.isdigit():
       guesses = int(guesses)
       guesses += 1
       
       if guesses < lowest_num or guesses > highest_num:
           print("That number is out of range")
           print(f"Please select a number between{lowest_num} and {highest_num}")
       elif guesses < answer:
           print("Too low! Try again!")
       elif guesses > answer:
           print("Too high! Try again!")
       else:
           print(f"CORRECT! The answer was {answer}")
           print(f"Number of guesses:{guesses}")
           is_running = False
           
           
    else:
        print("Invalid guess")
        print(f"Please select a number between{lowest_num} and {highest_num}")