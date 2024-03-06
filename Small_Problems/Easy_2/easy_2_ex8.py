def oddities(lists):
    return [lists[idx] for idx in range(len(lists)) if idx % 2 == 0]
    return lists[::2] # This also works

print(oddities([2, 3, 4, 5, 6]) == [2, 4, 6])  # True
print(oddities([1, 2, 3, 4]) == [1, 3])        # True
print(oddities(["abc", "def"]) == ['abc'])     # True
print(oddities([123]) == [123])                # True
print(oddities([]) == [])                      # True
