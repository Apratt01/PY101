my_list1 = [{"first": "value1"}, {"second": "value2"}, 3, 4, 5]
my_list2 = my_list1.copy()
my_list2[0]['first'] = 42

print(my_list1)


# my_list1 is initialized to a list with a bunch of things.
# my_list2 is initialized to a shallow copy of my_list2, or the list object
# A shallow copy makes a duplicate of the outermost values in an object.
# The dictionary objects inside the list are not duplicated, both my_list1 and
# my_list2 point to the same dicitonary object in memory. So any changes
# to the dictionary objects in my_list2 will mutate my_list1 also.
# my_list2[0]['first] is reassigned to the value 42
# this will print [{"first": 42}, {"second": "value2"}, 3, 4, 5]

