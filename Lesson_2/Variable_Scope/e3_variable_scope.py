num = 5

def my_func():
    global num
    num = 10

my_func()
print(num)

# This prints 10. The variable num is initialized to 5 on line 1. On line 4 the
# global keyword inside the function is used to reference the global variable
# num initialized on line 1. For that reason, on line 5, the  global variable 
# num is reassigned to 10 and then printed on line 8.