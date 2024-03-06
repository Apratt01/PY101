a = 42
b = 42
c = a

print(id(a) == id(b) == id(c))

# 42 is immutable and holds a unique place in memory.
# All initializations and reassignments pointing to 42, point to the same place
# in memory.  

# This prints True