def my_func():
    x = 15

    def inner_func1():
        x = 25
        print("Inner 1:", x)

    def inner_func2():
        print("Inner 2:", x)

    inner_func1()
    inner_func2()

my_func()

# The function my_func is defined on line 1. Within that function the local
# variable x is initialized on line 2 and assigned the value 15. The
# inner_func1 function is defined on line 4. Inside that function a new local
# variable x is initialized on line 5 to the value 25. The outer x cannot
# be reassigned in this way, the outer x remains 15, the inner x remains 25. The
# print function is called on the inner variable x. On line 8 the function 
# inner_func2 is defined and the function print is called on the outer local 
# variable x.  Because the inner_func1() variable x is within inner_func2() peer
# scope, it is not accessible. It can only access the variable x defined in the
# outer scope of my_func(). This should print Inner 1: 25 Inner 2: 15