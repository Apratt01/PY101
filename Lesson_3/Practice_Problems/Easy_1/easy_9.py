advice = "Few things in life are as important as house training your pet dinosaur."
# Expected return value:
# => 'Few things in life are as important as '

print(advice.split('house')[0])
print(advice.split('house')[1])

# .split method returns a list of strings split at the substring. The substring
# is excluded from all elements of the list, the space is included in the 2nd
# element.

