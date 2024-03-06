from datetime import datetime

def get_age():
    print("What is your age? ")
    age = input()
    
    while True:
        try:
            isinstance(int(age), int)
            if int(age) > 0:
                return int(age)
            else:
                print("That isn't valid, please enter as a number greater than "
                "zero. ")
                age = input()
        except ValueError:
            print("That isn't valid, please enter as a number greater than "
            "zero. ")
            age = input()
            
def get_retirement(person_age):
    print("At what age would you like to retire? ")
    retirement_age = input()
    
    while True:
        try: 
            isinstance(retirement_age, int)
            if int(retirement_age) >= person_age :
                return int(retirement_age)
            else:
                print("That isn't valid, please enter a number at that is equal to "
                "your current age or older. ")
                retirement_age = input()
        except ValueError:
            print("That isn't valid, please enter a number at that is equal to "
            "your current age or older. ")
            retirement_age = input()

def math(current_age, retirement):
    current_year = datetime.now().year
    years_to_go = retirement - current_age
    retirement_year = current_year + years_to_go
    return(current_year, years_to_go, retirement_year)
    
def output(now, future, years_left):
    print(f"It's {now}. You will retire in {future}.")
    print(f"You have only {years_left} years of work to go!")
    
def main():
    age = get_age()
    retirement_goal = get_retirement(age)
    this_year, years, future_year = math(age, retirement_goal)
    output(this_year, future_year, years)
    
main()
