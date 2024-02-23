import platform
import random
import json
import os

with open('rps_messages.json', 'r') as file:
    MESSAGES = json.load(file) # import JSON file

WINNING_SCORE = 5
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
        
def get_rules_choice():
    prompt(MESSAGES["rules_read"])
    answer = input()
    
    while answer.lower() not in ('y', 'yes', 'n', 'no'):
        prompt(MESSAGES["yes_or_no"])
        answer = input()
    
    answer = answer.lower()
    if answer in ('y', 'yes'):
        display_rules(answer)

def display_rules(answer):
    rules = '\n'.join(MESSAGES['rules'])
    print(rules.format(winning_number=WINNING_SCORE))
        
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
        return 'computer_wins'
    elif computer in GAME_CHOICES['wins'][player]:
        return 'player_wins'
    else:
        return 'ties'
        
def display_winner(player, computer, winner):
    
    prompt(MESSAGES["choice_recap"].format(player_choice=player,
        computer_choice=computer))
        
    if winner == 'player_wins':
        prompt(MESSAGES["player_win"])
    elif winner == 'computer_wins':
        prompt(MESSAGES["computer_win"])
    else:
        prompt(MESSAGES["tie"])
        
def game_score_tracker(winner, score_tracker):
    if winner in ('player_wins', 'computer_wins'):
        score_tracker[winner] += 1
    return score_tracker
    
def display_grand_winner(score_tracker):
    for winner, score in score_tracker.items():
        if score == WINNING_SCORE:
            game_winner = winner
            if game_winner == 'player_wins':
                prompt(MESSAGES["grand_winner"].format(winner="Player"))
            else:
                prompt(MESSAGES["grand_winner"].format(winner="Computer"))
    
def game_play():
    while True:
        score_tracker = {'player_wins': 0, 'computer_wins':0}
        list_of_scores = list(score_tracker.values())
        
        while WINNING_SCORE not in list_of_scores:
            
            player= get_player_choice()
            computer = get_computer_choice()
            winner = select_winner(player, computer)
            display_winner(player, computer, winner)
            score_tracker = game_score_tracker(winner, score_tracker)
            list_of_scores = list(score_tracker.values())
            print(score_tracker)
        display_grand_winner(score_tracker)
        break


def main():
    clear_screen()
    prompt(MESSAGES['welcome'])
    clear_screen()
    get_rules_choice()
    game_play()
    
main()
