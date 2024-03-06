str1 = "Come over here!"  # True
str2 = "What's up, Doc?"  # False

print('yes') if str1[-1] == "!" else print('no')
print('yes') if str2.endswith('!') else print('no')