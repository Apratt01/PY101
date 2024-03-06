def is_dot_separated_ip_address(input_string):
    if input_string.count('.') != 3:
        print(input_string.count('.'))
        return False 
    dot_separated_words = input_string.split(".")
    while len(dot_separated_words) > 0:
        word = dot_separated_words.pop()
        if not is_an_ip_number(word):
            return False

    return True
    
def is_an_ip_number(str):
    if str.isdigit():
        number = int(str)
        return 0 <= number <= 255
    return False
    
print(is_dot_separated_ip_address('1'))
print(is_dot_separated_ip_address('1.2.3.4'))
print(is_dot_separated_ip_address('1.2.3.four'))
