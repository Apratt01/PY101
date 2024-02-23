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

def get_player_choice():

    while True:
        combined_list = []
        for initial, word in GAME_CHOICES['choices'].items():
            prompt(MESSAGES['choose'].format(key=initial, value=word))
            combined_list.append(initial)
            combined_list.append(word)
        choice = input()

        while choice.lower() not in combined_list:
            prompt(MESSAGES["invalid_choice"])
            choice = input()

        player = GAME_CHOICES['choices'][choice]
        return player

def get_computer_choice():
    list_of_words = []
    
    for _, word in GAME_CHOICES['choices'].items():
        list_of_words.append(word)
        
    computer = random.choice(list_of_words)
    return computer
    
def select_winner(player, computer):
    
    if player in GAME_CHOICES['wins'][computer]:
        return 'computer'
    elif computer in GAME_CHOICES['wins'][player]:
        return 'player'
    else:
        return 'ties'
        
def display_winner(player, computer, winner):
    
    prompt(MESSAGES["choice_recap"].format(player_choice=player,
        computer_choice=computer))
        
    if winner == 'player':
        prompt(MESSAGES["player_win"])
    elif winner == 'computer':
        prompt(MESSAGES["computer_win"])
    else:
        prompt(MESSAGES["tie"])
        
def game_score_tracker(winner):
    player_wins = 0
    computer_wins = 0
    if winner == 'player':
        player_wins += 1
    elif winner == 'computer':
        computer_wins += 0
        
    return player_wins, computer_wins
    

def game_round():
    player= get_player_choice()
    computer = get_computer_choice()
    winner = select_winner(player, computer)
    display_winner(player, computer, winner)
    player_wins, computer_wins = game_score_tracker(winner)
    print(player_wins, computer_wins)

def main():
    clear_screen()
    game_round()

main()
