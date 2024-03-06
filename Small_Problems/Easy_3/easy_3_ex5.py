def triangle(number):
    space = " " * number
    star = "*"
    
    for num in range(number):
        space = space[:-1]
        print(space + star)
        star += "*"
        
triangle(5)
triangle(9)

        