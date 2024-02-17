import platform
import random
import json
import os

with open('rps_messages.json', 'r') as file:
    MESSAGES = json.load(file) # import JSON file

VALID_CHOICES_EN = ['rock', 'paper', 'scissors'];
VALID_CHOICES_SP = ['roca', 'papel', 'tijeras'];

language = MESSAGES["en"]

def prompt(message):    
    print(f"==> {message}")

def ask_language():
    choices = ['en', 'sp', 'english', 'spanish', 'español']
    prompt(MESSAGES['en']["language"])
    language = input()

    while language.lower() not in choices:
        invalid = '\n'.join("invalid_language")
        prompt(invalid)
        language = input()

    language_lower = language.lower()
    return language_lower

def choose_language(language):

    if language in ('en', 'english'):
        return MESSAGES["en"]

    return MESSAGES["sp"]


def clear_screen():
    os_name = platform.system()

    if os_name == 'Windows':
        os.system('cls')  # Clear screen on Windows
    else:
        os.system('clear')  # Clear screen on Unix/Linux/Mac

def display_winner(player, computer):
    prompt(language["choice_recap"].format(player_choice=player,
        computer_choice=computer))

    if ((player == "rock" and computer == "scissors") or
        (player == "paper" and computer == "rock") or
        (player == "scissors" and computer == "paper")):
        prompt(language["player_win"])
    elif ((player == "rock" and computer == "paper") or
          (player == "paper" and computer == "scissors") or
          (player == "scissors" and computer == "rock")):
        prompt(language["computer_win"])
    else:
        prompt(language["tie"])

while True:
    prompt(language["choose"])
    prompt({", ".join(VALID_CHOICES_EN)})
    choice = input()

    while choice not in VALID_CHOICES_EN:
        prompt(language["invalid_choice"])
        choice = input()

    computer_choice = random.choice(VALID_CHOICES_EN)

    display_winner(choice, computer_choice)

    prompt("Do you want to play again (y/n)?")
    answer = input().lower()
    while answer and answer[0] != "n" and answer[0] != "y":
        prompt(language["yes_or_no"])
        answer = input().lower()

    if answer[0] != "y":
        break

def main():
    clear_screen()
    global language
    language = ask_language()
    language = choose_language(language)
    clear_screen()
    
main()