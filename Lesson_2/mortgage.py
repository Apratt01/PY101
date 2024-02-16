import platform
import json
import os

with open('mortgage_messages.json', 'r') as file:
    MESSAGES = json.load(file) # import JSON file

MONTHS_IN_YEAR = 12
DECIMAL_CONVERSION = 100

def prompt(message):
    print(f"==> {message}")

def clear_screen():
    os_name = platform.system()

    if os_name == 'Windows':
        os.system('cls')  # Clear screen on Windows
    else:
        os.system('clear')  # Clear screen on Unix/Linux/Mac

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

def get_loan_amount():
    prompt(language_message["loan_amount"])
    amount = input()

    while invalid_loan_amount(amount):
        prompt(language_message["invalid_number"])
        amount = input()

    return float(amount)

def get_interest_rate():
    prompt(language_message["int_rate"])
    apr = input()

    while invalid_number(apr):
        prompt(language_message["invalid_number"])
        apr = input()

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
    prompt(language_message["loan_years"])
    years = input()

    while invalid_number(years):
        prompt(language_message["invalid_number"])
        years = input()
    return int(years)

def get_loan_months():
    prompt(language_message["loan_months"])
    years = input()

    while invalid_number(years):
        prompt(language_message["invalid_number"])
        years = input()
    return int(years)

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
    display_recap(loan, interest, months)
    display_totals(monthly_payment, total_paid, interest_paid)

def display_recap(loan, interest, months):
    recap_message = '\n'.join(language_message['recap'])
    prompt(recap_message.format(loan_amount=loan, apr=interest, time=months))


def display_totals(payment, total_paid, total_interest):
    totals_message = '\n'.join(language_message['result'])
    prompt(totals_message.format(monthly_payment=payment,
        amount_paid=total_paid,interest_paid=total_interest))

def repeat():
    prompt(language_message["repeat"])
    answer = input()

    if answer.lower() == 'yes' or answer.lower() == 'y':
        start()
    else: prompt(language_message["no"])


def start():
    clear_screen()
    loan = get_loan_amount()
    interest_rate = get_interest_rate()
    months_of_loan = get_loan_duration()
    math(loan, interest_rate, months_of_loan)
    repeat()

def main():
    global language_message
    clear_screen()
    prompt(MESSAGES["en"]["welcome"])
    prompt(MESSAGES["sp"]["welcome"])
    language_choice = ask_language()
    language_message = choose_language(language_choice)
    start()

main()
    