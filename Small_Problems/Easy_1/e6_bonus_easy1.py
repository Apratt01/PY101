# Gets the input as a single string with built in spaces, validtes, and then
# returns as a list of integers
def number():
    while True:
        numbers = input("Please enter a list of integers greater than zero and "
                        "separated by a space: ")
        numbers_list = numbers.split(" ")
        numbers_valid = []
        for number in numbers_list:
            if number.isnumeric() and int(number) > 0:
                numbers_valid.append(int(number))
            else:
                numbers_valid = False    
                break
        if numbers_valid:
            return numbers_valid
        else:
            print("That is not a list of integers greater than zero. Please "
                  "try again.")

# Gets users choice sum or produce and validates. Case sensitive is ignored.
def choice(): 
    while True:
        choice = input("Enter 's' to compute the sum, or \"p\" to compute the "
                        "product. ")
        if choice.lower() == 's' or choice.lower() == 'p':
            return choice.lower()
        else:
            print("That is not a valide selection. Please try again")

# Chooses which mathematical branch function to call based on user choice
def which_choice(number, choice):
    sum_of_integer(number) if choice == 's' else product_of_integer(number)

# Takes the list of numbers and runs them through the math and prints each out.
# For future enhancement, identify each number as the 1st, 2nd, etc.
def sum_of_integer(number):
    total = 0
    for integer in number:
        for num in range(1, integer + 1):
            total += num
        print(f"The sum of the integers between 1 and {integer} is {total}.")
        total = 0


def product_of_integer(number):
    total = 1
    for integer in number:
        for num in range(1, integer + 1):
            total *= num
        print(f"The product of the integers between 1 and {integer} is {total}."
        )
        total = 1    

# Initiates the program    
def main():
    number_entered = number()
    choice_entered = choice()
    which_choice(number_entered, choice_entered)
    
main()