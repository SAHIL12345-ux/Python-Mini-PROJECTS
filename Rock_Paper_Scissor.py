import random

options = ("rock" , "paper ","scissor")
running = True
while running:
    
    player = None
    computer = random.choice(options)
 
    while player  not in options:
        player = input("Enter a choice(rock , paper ,scissor):")
    print(f"Player: {player}")
    print(f"Coomputer:{computer}")
    if player == computer:
        print("It's a tie")
    elif player == "rock"  and computer == "scissor":
        print("you win!")
    elif player == "paper"  and computer == "rock":
        print("you win!")
    elif player == "scissor" and computer == "paper":
        print("you win")
    else:
        print("you lose!")
    if not input("play_again ? (y/n): ").lower() == "y":
         running = False

print("Thanks for Playing!")