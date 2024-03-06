def mess_with_vars(one, two, three):
    one = two # one is now 'two'
    two = three # two is now 'three'
    three = one # three is now 'two'

one = ["one"]
two = ["two"]
three = ["three"]

mess_with_vars(one, two, three)

print(f"one is: {one}") # the original object is not modified, this prints 'one'
print(f"two is: {two}") # same, this prints 'two'
print(f"three is: {three}") # same, this prints 'three'

def mess_with_vars(one, two, three):
    one = ["two"]
    two = ["three"]
    three = ["one"]

one = ["one"]
two = ["two"]
three = ["three"]

mess_with_vars(one, two, three)

print(f"one is: {one}") # same result, the function does not modify the original
print(f"two is: {two}")
print(f"three is: {three}")

def mess_with_vars(one, two, three):
    one[0] = "two"
    two[0] = "three"
    three[0] = "one"

one = ["one"]
two = ["two"]
three = ["three"]

mess_with_vars(one, two, three)

print(f"one is: {one}") # index syntax will mutate the original object, this prints 'two'
print(f"two is: {two}") # because lists are mutable and references are passed to functions
print(f"three is: {three}") # the elements inside the lists are modified, so the original list is mutated.


