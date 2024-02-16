def outer():
    outer_var = 'Hello'

    def inner():
        inner_var = 'World'
        print(outer_var, inner_var)

    inner()

outer()

# The outer() function defines a local variable outer_var with the value 'Hello'
# Inside it the inner function is defined, which has it's own local variable
# inner_var with the value 'world'. When inner() is called within outer(), both
# outer_var and inner_var are printed using the print(outer_var, inner_var)
# statement, resulting in the output Hello World.