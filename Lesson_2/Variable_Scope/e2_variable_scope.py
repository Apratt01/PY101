num = 5

def my_func():
    num = 10

my_func()
print(num)

# The variable num is initialized to 5 on line 1. In the my_func method
# a different num is initialized to 10. The 1st num on line 1 cannot be 
# reassigned within the function. It is not passed to the function as an
# argument, it is not returned as an argument, and it is not mutated by
# the function. This is an example of variable shadowing.