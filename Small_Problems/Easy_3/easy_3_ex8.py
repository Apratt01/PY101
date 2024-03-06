def get_grade(num1, num2, num3):
    sum_total = num1 + num2 + num3
    avg = sum_total / 3.0
    
    if avg < 60:
        return 'F'
    elif avg < 70:
        return 'D'
    elif avg < 80:
        return 'C'
    elif avg < 90:
        return 'B'
    else:
        return 'A'

print(get_grade(95, 90, 93) == "A")      # True
print(get_grade(50, 50, 95) == "D")      # True