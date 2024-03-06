def is_color_valid(color):
    return color in ('blue', 'green')

def is_color_valid1(color):
    return color in ['blue', 'green']

print(is_color_valid('blue'))
print(is_color_valid1('red'))
