def xor(input1, input2):
    if input1 and input2:
        return False
    elif input1 or input2:
        return True
    

print(xor(5, 0) == True)
print(xor(False, True) == True)
print(xor(1, 1) == False)
print(xor(True, True) == False)