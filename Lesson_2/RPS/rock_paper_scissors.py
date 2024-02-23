import platform
import random
import json
import os

with open('rps_messages.json', 'r') as file:
    MESSAGES = json.load(file) # import JSON file

GAME_CHOICES = {
    'wins': {
        'scissors': ['paper', 'lizard'],
        'paper': ['rock', 'spock'],
        'rock': ['lizard', 'scissors'],
        'lizard': ['spock', 'paper'],
        'spock': ['scissors', 'rock']
        },
    'choices': {
        's': 'scissors',
        'p': 'paper',
        'r': 'rock',
        'l': 'lizard',
        'sp': 'spock'
        }
    }


def prompt(message):    
    print(f"==> {message}")

def clear_screen():
    os_name = platform.system()

    if os_name == 'Windows':
        os.system('cls')  # Clear screen on Windows
    else:
        os.system('clear')  # Clear screen on Unix/Linux/Mac

def display_winner(player, computer):
    prompt(MESSAGES["choice_recap"].format(player_choice=player,
        computer_choice=computer))
    
    if player in GAME_CHOICES['wins'][computer]:                                                                                  
        prompt(MESSAGES["computer_win"])                                                                                                                                                        
    elif computer in GAME_CHOICES['wins'][player]:                                                                      
        prompt(MESSAGES["player_win"])                                                                                                                                               
    else:                                                                                                                                                                               
        prompt(MESSAGES["tie"])
                
def get_choices():

    while True:
        list_of_intials = []
        list_of_words = []
        combined_list = []
        for initial, word in GAME_CHOICES['choices'].items():
            prompt(MESSAGES['choose'].format(key=initial, value=word))
            list_of_words.append(word)
            combined_list.append(initial)
            combined_list.append(word)
        choice = input()
        
        while choice.lower() not in combined_list:
            prompt(MESSAGES["invalid_choice"])
            choice = input()
            
        computer = random.choice(list_of_words)
        player = GAME_CHOICES['choices'][choice]
        return computer, player
            
def game_round():
    computer, player = get_choices()
    return computer, player
    
computer, player = game_round()
print(computer, player)
display_winner(player, computer)

#     display_winner(choice, computer_choice)

#     prompt("Do you want to play again (y/n)?")
#     answer = input().lower()
#     while answer and answer[0] != "n" and answer[0] != "y":
#         prompt(language["yes_or_no"])
#         answer = input().lower()

#     if answer[0] != "y":
#         break

# def main():
#     clear_screen()
#     global language
#     language = ask_language()
#     language = choose_language(language)
#     clear_screen()
    
# main()