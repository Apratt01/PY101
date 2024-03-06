def penultimate(str1):
    list_of_words = str1.split(' ')
    return list_of_words[-2]
        


# These examples should print True
print(penultimate("last word") == "last")
print(penultimate("Launch School is great!") == "is")