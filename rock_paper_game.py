import random

choices = ["rock", "paper", "scissors"]

player = input("Choose rock, paper or scissors: ").lower()
computer = random.choice(choices)

if player == computer:
    print(f"It's a tie! Both chose {player}.")

elif (
    (player == "rock" and computer == "scissors")
    or (player == "paper" and computer == "rock")
    or (player == "scissors" and computer == "paper")
):
    print(f"You win! {player} beats {computer}.")

else:
    print(f"Computer wins! {computer} beats {player}.")