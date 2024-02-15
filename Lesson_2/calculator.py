import json

with open('calculator_messages.json', 'r') as file:
    MESSAGES = json.load(file)
    
def prompt(message):
    print(f"==> {message}")

def ask_language():
    choices = ['en', 'sp', 'english', 'spanish', 'español']
    prompt(MESSAGES["language_en"])
    prompt(MESSAGES["language_sp"])
    language = input()
    
    while language.lower() not in choices:
        prompt(MESSAGES["invalid_language_en"])
        prompt(MESSAGES["invalid_language_sp"])
        language = input()
    language_lower = language.lower()
    return choose_language(language_lower)
    
def choose_language(language):
    if language == 'en' or language == 'english':
        return MESSAGES['en']
    else:
        return MESSAGES['sp']

def invalid_number(number_str):
    try:
        int(number_str)
    except ValueError:
        return True

    return False

def number_one():
    prompt(language_message["first_number"])
    number1 = input()

    while invalid_number(number1):
        prompt(language_message["invalid_number"])
        number1 = input()
    return number1
        
def number_two():
    prompt(language_message["second_number"])
    number2 = input()

    while invalid_number(number2):
        prompt(language_message["invalid_number"])
        number2 = input()
    return number2

def operation_choice():
    operation_message = '\n'.join(language_message['operation_message'])
    prompt(operation_message)
    operation = input()

    while operation not in ["1", "2", "3", "4"]:
        prompt(language_message["invalid_choice"])
        operation = input()
    return operation

def math(number1, number2, choice):
    output = 0
    match choice:
        case "1":
            output = int(number1) + int(number2)
        case "2":
            output = int(number1) - int(number2)
        case "3":
            output = int(number1) * int(number2)
        case "4":
            output = int(number1) / int(number2)
    prompt(language_message["result"].format(variable=output))
    
def repeat():
    prompt(language_message["repeat"])
    answer = input()
    
    if answer.lower() == 'yes':
        print(language_message["yes"])
        main()
    else: print(language_message["no"])
    

def main():
    number1 = number_one()
    number2 = number_two()
    choice = operation_choice()
    math(number1, number2, choice)
    repeat()

prompt(MESSAGES["en"]["welcome"])
prompt(MESSAGES["sp"]["welcome"])
language_message = ask_language()

main()