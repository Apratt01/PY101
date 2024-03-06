dictionary = {'first': [1]}
num_list = dictionary['first']
num_list.append(2)

print(num_list) # [1, 2]
print(dictionary) # {'first': [1]}

# num_list is initialized to a reference of the original list in the dictionary.
# As a result the append method modifies the original object.
# To prevent this, use the copy method when initializing num_list. This references
# a copy of the object instead of a refernce directly to the object, preventing
# mutation of the original object.
# Or use slicing when initializing num_list, as slicing returns a new list.
# Any methods or functions will affect the new list, not the original object.

