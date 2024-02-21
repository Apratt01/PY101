import platform
import json
import os

with open('mortgage_messages.json', 'r') as file:
    MESSAGES = json.load(file) # import JSON file

MONTHS_IN_YEAR = 12
DECIMAL_CONVERSION = 100
language_choice = None # Global variable - changed depending on user input

def prompt(message):
    print(f"==> {message}")

def clear_screen():
    os_name = platform.system()

    if os_name == 'Windows':
        os.system('cls')  # Clear screen on Windows
    else:
        os.system('clear')  # Clear screen on Unix/Linux/Mac

def clean_input(input_value):
    symbols = ['$', '%', ',', '#']
    for symbol in symbols:
        if symbol in input_value:
            input_value = input_value.replace(symbol, '')
    return input_value

def get_language():
    choices = ['en', 'es', 'english', 'spanish', 'español']
    prompt(MESSAGES["language_en"])
    prompt(MESSAGES["language_sp"])
    language = input()

    while language.lower() not in choices:
        prompt(MESSAGES["invalid_language_en"])
        prompt(MESSAGES["invalid_language_sp"])
        language = input()

    language_lower = language.lower()
    return language_lower

def choose_language(language):

    if language in ('en', 'english'):
        return MESSAGES['en']

    return MESSAGES['sp']

def invalid_loan_amount(loan_str):
    try:
        float(loan_str)
        if float(loan_str) <= 0:
            return True
    except ValueError:
        return True

    return False

def invalid_number(num_str):
    try:
        float(num_str)
        if float(num_str) < 0:
            return True
    except ValueError:
        return True

    return False

def invalid_integer(num_str):
    try:
        int(num_str)
        if int(num_str) < 0:
            return True
    except ValueError:
        return True

    return False

def get_loan_amount():
    prompt(language_message["loan_amount"])
    amount = input()
    amount = clean_input(amount)

    while invalid_loan_amount(amount):
        prompt(language_message["invalid_number"])
        amount = input()
        amount = clean_input(amount)

    return float(amount)

def get_interest_rate():
    prompt(language_message["int_rate"])
    apr = input()
    apr = clean_input(apr)

    while invalid_number(apr):
        prompt(language_message["invalid_number"])
        apr = input()
        apr = clean_input(apr)

    return float(apr)

def get_loan_duration():
    total_months = 0

    while total_months == 0:
        years = get_loan_years()
        months = get_loan_months()
        total_months = years_to_months(years, months)
        if total_months == 0:
            prompt(language_message["zero_months"])
    return total_months

def years_to_months(years, months):
    if years > 0:
        total_months = years * MONTHS_IN_YEAR + months
    else:
        total_months = months
    return total_months

def get_loan_years():
    year_prompt = '\n'.join(language_message['loan_years'])
    prompt(year_prompt)
    years = input()
    years = clean_input(years)

    while invalid_integer(years):
        prompt(language_message["invalid_number"])
        years = input()
        years = clean_input(years)

    return int(years)

def get_loan_months():
    month_prompt = '\n'.join(language_message['loan_months'])
    prompt(month_prompt)
    months = input()
    months = clean_input(months)

    while invalid_integer(months):
        prompt(language_message["invalid_number"])
        months = input()
        months = clean_input(months)
    return int(months)

def math(loan, interest, months):
    if interest == 0:
        monthly_rate = 0
        monthly_payment = loan / months
    else:
        monthly_rate = interest / DECIMAL_CONVERSION / MONTHS_IN_YEAR
        monthly_payment = loan * (monthly_rate / (1 - (1 + monthly_rate) **
            (-months)))

    total_paid = monthly_payment * months
    interest_paid = total_paid - loan

    return monthly_payment, total_paid, interest_paid


def display_recap(loan, interest, months):
    recap_message = '\n'.join(language_message['recap'])
    prompt(recap_message.format(loan_amount=loan, apr=interest, time=months))


def display_totals(payment, total_paid, total_interest):
    totals_message = '\n'.join(language_message['result'])
    prompt(totals_message.format(monthly_payment=payment,
        amount_paid=total_paid,interest_paid=total_interest))

def repeat():
    prompt(language_message["repeat"])
    user_answer = input()

    return user_answer

def start():
    clear_screen()
    loan = get_loan_amount()
    interest_rate = get_interest_rate()
    months_of_loan = get_loan_duration()
    payment, total_paid, int_paid = math(loan, interest_rate, months_of_loan)
    display_recap(loan, interest_rate, months_of_loan)
    display_totals(payment, total_paid, int_paid)


def main():
    global language_message
    clear_screen()
    prompt(MESSAGES["en"]["welcome"])
    prompt(MESSAGES["sp"]["welcome"])
    language_choice = get_language()
    language_message = choose_language(language_choice)
    start()

main()

while True:
    answer = repeat()
    choice = ('y', 'Yes', 'Y', 'yes', 'YES')
    if answer in choice:
        start()
    else:
        prompt(language_message["no"])
        break
