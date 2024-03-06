def print_in_box(string):
    dash = '-' * (len(string) + 2)
    space = ' ' * (len(string) + 2)
    
    print(f"+{dash}+")
    print(f"|{space}|")
    print(f"| {string} |")
    print(f"|{space}|")
    print(f"+{dash}+")
    
print_in_box('To boldly go where no one has gone before.')
print_in_box('')