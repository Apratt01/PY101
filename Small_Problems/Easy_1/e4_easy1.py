def input_type():
    print("Welcome to the size of the room calclator!")
    while True:
        choice = input("First, please choose if you are working with 'm' for "
                        "meters or 'f' for feet. ")
        if choice.lower() == 'f' or choice.lower() == 'm':
            return choice.lower()
        else:
            print("Sorry that is not a valid choice. Please try again")
                

def length_of_room():
    while True:
        length = input("How long is the room? ")
        try:
            length_float = float(length)
            if length_float > 0:
                return length_float
            else:
                print("Length must be a postive number greater than zero. " 
                       "Please try again.")
        except ValueError:
            print("Sorry that is not a valid number. Please try again")
    
def width_of_room():
    while True:
        width = input("How wide is the room? ")
        try:
            width_float = float(width)
            if width_float > 0:
                return width_float
            else:
                print("Width must be a postive number greater than zero. "
                      "Please try again.")
        except ValueError:
            print("Sorry that is not a valid number, please try again")
    
    
def area(length, width):
    return length * width

def conversion(area, choice):
    if choice == 'f':
        area_in_meters = area * 0.092903
        print(f"The area of the room is {area:.2f} feet, ({area_in_meters:.2f} "
        "in meters).")
    else:
        area_in_feet = area * 10.7639
        print(f"The area of the room is {area:.2f} meters, ({area_in_feet:.2f} "
        "in feet).")

def main():
    choice_of_input = input_type()
    length = length_of_room()
    width = width_of_room()
    area_calculated = area(length, width)
    conversion(area_calculated, choice_of_input)
    
main()
    
    
    
    