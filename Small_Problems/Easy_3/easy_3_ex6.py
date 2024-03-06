def get_choices():
    list_of_choices = ['noun', 'verb', 'adjective', 'adverb']
    users = []
    count = 0
    temp = ''
    
    while count < 4:
        temp = input(f"Please enter a {list_of_choices[count]}: ")
        
        while True:
            if (not (temp.isdigit() or temp.replace('.', '',1).isdigit()) 
                and temp != ''):
                users.append(temp)
                temp = ''
                break
            else:
                print("That is not a valid input, please try again")
                temp = input(f"Please enter a {list_of_choices[count]}: ")
        count += 1
        
    return users

def output(list_of_words):
    print(f"Do you {list_of_words[1]} your {list_of_words[2]} "
    f"{list_of_words[0]} dog {list_of_words[3]}? That's hilarious!")
    
    print(f"The {list_of_words[2]} {list_of_words[0]} {list_of_words[1]}s "
    f"{list_of_words[3]} over the lazy {list_of_words[0]}.")
    
    print(f"The {list_of_words[0]} {list_of_words[3]} {list_of_words[1]}s up "
    f"to Joe's {list_of_words[2]} turtle.")
    
def main():
    user_choices = get_choices()
    output(user_choices)
    
main()
