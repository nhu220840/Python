import random

options = ("rock", "paper", "scissors")
playing = True

while playing:
    player = None
    computer = random.choice(options)

    while player not in options: 
        player = input("Select your choice (rock, paper, scissors): ")

    print(f"Player: {player}")
    print(f"Computer: {computer}")

    if player == computer:
        print("It is a tie!")
    elif ((player == "rock" and computer == "scissors")
        or (player == "scissors" and computer == "paper") 
        or (player == "paper" and computer == "rock")):
        print("You win!!!")
    else:
        print("You lose!")

    if input("Can you play again? (y/n): ").lower() == "n":
        playing = False

print("Thanks for playing!") 
