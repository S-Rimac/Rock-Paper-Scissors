import random

game = ["rock", "paper", "scissors"]
player = input("Choose Rock, Paper or Scissors?").lower()
comp = random.choice(game)

while player not in game:
    print("Enter valid choice")
    player = input("Please enter one of options: ")
print(f"Player choose:{player.capitalize()}")
print(f"Comp choose:{comp.capitalize()}")

if player == game:
    print("It's a tie")
elif player == "paper" and comp == "rock":
    print("You Win!")
elif player == "rock" and comp == "scissors":
    print("You Win")
elif player == "scissors" and comp == "paper":
    print("You win")
else:
    print("You lose")
    
