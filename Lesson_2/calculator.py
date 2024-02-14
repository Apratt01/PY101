def prompt(message):
    print(f"==> {message}")

def invalid_number(number_str):
    try:
        int(number_str)
    except ValueError:
        return True

    return False

def number_one():
    prompt("What's the first number?")
    number1 = input()

    while invalid_number(number1):
        prompt("Hmm... that doesn't look like a valid number.")
        number1 = input()
    return number1
        
def number_two():
    prompt("What's the second number?")
    number2 = input()

    while invalid_number(number2):
        prompt("Hmm... that doesn't look like a valid number.")
        number2 = input()
    return number2

def operation_choice():
    prompt("What operation would you like to perform?\n1) Add 2) Subtract 3) "
       "Multiply 4) Divide")
    operation = input()

    while operation not in ["1", "2", "3", "4"]:
        prompt("You must choose 1, 2, 3, or 4")
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
    prompt(f"The result is {output}")
    
def repeat():
    prompt("Would you like to do another calculation? Yes to go again!")
    answer = input()
    
    if answer.lower() == 'yes':
        print("Great, let's go again!")
        main()
    else: print("Thank you for playing!")
    

def main():
    prompt("Welcome to Calculator!")
    number1 = number_one()
    number2 = number_two()
    choice = operation_choice()
    math(number1, number2, choice)
    repeat()
    
main()