import random

def name():
    name = input("What is the name of the person? ")
    return name
    
def output(person, age):
    if person == "":
        person = 'Teddy'
    
    print(f"{person} is {age} years old!")

def main():
    age = random.randint(20, 100)
    name_of_person = name()
    output(name_of_person, age)
    
main()