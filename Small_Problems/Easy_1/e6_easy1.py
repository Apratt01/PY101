def number():
    while True:
        number = input("Please enter an integer greater than 0: ")
        try:
            number = int(number)
            if number > 0:
                return number
            else:
                print("The number must be greater than zero. Please try again")
        except ValueError:
            print("That is not a valid number. Please try again")
            
def choice():
    while True:
        choice = input("Enter 's' to compute the sum, or \"p\" to compute the "
                        "product. ")
        if choice.lower() == 's' or choice.lower() == 'p':
            return choice.lower()
        else:
            print("That is not a valide selection. Please try again")

def math(number, choice):
    if choice == 's':
        total = sum_of_integer(number)
        output_sum(number, total)
    else:
        total = product_of_integer(number)
        output_product(number, total)
        
def sum_of_integer(number):
    total = 0
    for num in range(1, number + 1):
        total += num
    return total

def product_of_integer(number):
    total = 1
    for num in range(1, number + 1):
        total *= num
    return total

def output_sum(number, total):
    print(f"The sum of the integers between 1 and {number} is {total}.")
    
def output_product(number, total):
    print(f"The product of the integers between 1 and {number} is {total}.")
    
def main():
    number_entered = number()
    choice_entered = choice()
    math(number_entered, choice_entered)
    
main()


