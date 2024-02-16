import random

validChoices = ["rock", "paper", "scissors"]

def prompt(message):
    print(f"==> {message}")

def display_winner(player, computer):
    prompt(f"You chose {player}, computer chose {computer}")

    if ((player == "rock" and computer == "scissors") or
        (player == "paper" and computer == "rock") or
        (player == "scissors" and computer == "paper")):
        prompt("You win!")
    elif ((player == "rock" and computer == "paper") or
          (player == "paper" and computer == "scissors") or
          (player == "scissors" and computer == "rock")):
        prompt("Computer wins!")
    else:
        prompt("It's a tie!")

while True:
    prompt(f'Choose one: {", ".join(validChoices)}')
    choice = input()

    while choice not in validChoices:
        prompt("That's not a valid choice")
        choice = input()

    computer_choice = random.choice(validChoices)

    display_winner(choice, computer_choice)

    prompt("Do you want to play again (y/n)?")
    answer = input().lower()
    while answer and answer[0] != "n" and answer[0] != "y":
        prompt('Please enter "y" or "n".')
        answer = input().lower()

    if answer[0] != "y":
        break