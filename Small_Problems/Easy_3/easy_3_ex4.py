def stringy(number):
    string_bits = ''
    
    for num in range(number):
        string_bits += '1' if num % 2 == 0 else '0'
    
    return string_bits



print(stringy(6) == "101010")           # True
print(stringy(9) == "101010101")        # True
print(stringy(4) == "1010")             # True
print(stringy(7) == "1010101")          # True