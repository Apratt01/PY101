def center_of(string):
    center = (len(string)) // 2
    if len(string) % 2 == 0:
        return string[center-1] + string[center]
    else:
        return string[center]


print(center_of('I Love Python!!!') == "Py")    # True
print(center_of('Launch School') == " ")        # True
print(center_of('Launchschool') == "hs")        # True
print(center_of('Launch') == "un")              # True
print(center_of('Launch School is #1') == "h")  # True
print(center_of('x') == "x")                    # True