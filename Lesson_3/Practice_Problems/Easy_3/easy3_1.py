numbers = [1, 2, 3, 4]

numbers1 = numbers
numbers1.clear()

numbers2 = numbers
while numbers2:
    numbers2.pop()


print(numbers1)
print(numbers2)

