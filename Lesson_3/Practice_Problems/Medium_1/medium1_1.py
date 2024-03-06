str1 = "The Flintstones Rock!"
space = ""
for number in range(10):
    print(space + str1)
    space += ' '
    
# or

for padding in range(1, 11):
    print(" " * padding + "The Flintstones Rock!")

 