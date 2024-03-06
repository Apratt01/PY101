answer = 42

def mess_with_it(some_number):
    return some_number + 8 # 42 + 8 = 50

new_answer = mess_with_it(answer) # 50

print(answer - 8) # 34, answer is not mutated by the function


