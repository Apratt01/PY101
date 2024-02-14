import json

with open('calculator_messages.json', 'r') as file:
    MESSAGES = json.load(file)

def prompt(message):
    print(f"==> {message}")

def invalid_number(number_str):
    try:
        int(number_str)
    except ValueError:
        return True

    return False

def number_one():
    prompt(MESSAGES["first_number"])
    number1 = input()

    while invalid_number(number1):
        prompt(MESSAGES["invalid_number"])
        number1 = input()
    return number1
        
def number_two():
    prompt(MESSAGES["second_number"])
    number2 = input()

    while invalid_number(number2):
        prompt(MESSAGES["invalid_number"])
        number2 = input()
    return number2

def operation_choice():
    operation_message = '\n'.join(MESSAGES['operation_message'])
    prompt(operation_message)
    operation = input()

    while operation not in ["1", "2", "3", "4"]:
        prompt(MESSAGES["invalid_choice"])
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
    prompt(MESSAGES["result"].format(variable=output))
    
def repeat():
    prompt(MESSAGES["repeat"])
    answer = input()
    
    if answer.lower() == 'yes':
        print(MESSAGES["yes"])
        main()
    else: print(MESSAGES["no"])
    

def main():
    number1 = number_one()
    number2 = number_two()
    choice = operation_choice()
    math(number1, number2, choice)
    repeat()

prompt(MESSAGES["welcome"])

main()