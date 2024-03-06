def foo(param="no"):
    return "yes"

def bar(param="no"):
    return param == "no" and foo() or "no"
    
bar(foo())

# The foo function returns 'yes'
# 'yes' is passed to bar()
# 'The and statement evalutes to False because param == 'yes'
# This returns "no"