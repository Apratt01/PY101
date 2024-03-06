def is_double_doube(num):
    str_num = str(num)
    mid = len(str_num) // 2
    left, right = str_num[:mid], str_num[mid:]
    return (len(str_num) % 2 == 0) and (left == right)

def twice(num):
    return num if is_double_doube(num) else num * 2


print(twice(37) == 74)                  # True
print(twice(44) == 44)                  # True
print(twice(334433) == 668866)          # True
print(twice(444) == 888)                # True
print(twice(107) == 214)                # True
print(twice(103103) == 103103)          # True
print(twice(3333) == 3333)              # True
print(twice(7676) == 7676)              # True