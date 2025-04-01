import random

running = True

while running:
    choices = ["rock", "paper", "scissors"] # rock = hajar, paper = waraka, scissors = mikas
    computer = random.choice(choices)
    player = input("\nChoose rock, paper, or scissors: ").lower()
        
    if player not in choices:
        print("Invalid choice! Please choose rock, paper, or scissors.")
        
    print(f"Computer chose: {computer}")
        
    if player == computer:
        print("It's a tie! (no winner no loser) ")
    elif (player == "rock" and computer == "scissors") or \
        (player == "scissors" and computer == "paper") or \
        (player == "paper" and computer == "rock"):
        print("You win!")
    else:
        print("You lose!")

    repeat = input("play again ? (y/n)").lower()
    if repeat == 'n': 
        running = False
    elif repeat == 'y':
        continue
    