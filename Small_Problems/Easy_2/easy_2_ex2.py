def greeting(name):
    if name[-1:] == '!':
        print(f"HELLO {name.upper()} WHY ARE WE YELLING?")
    else:
        print(f"Hello {name}")

def main():
    user_input = input("What is your name? ")
    greeting(user_input.strip())

main()
