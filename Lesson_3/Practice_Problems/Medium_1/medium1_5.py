import math

nan_value = float("nan")

print(nan_value == float("nan")) # prints False

# To check for nan use the math isnan function

print(math.isnan(nan_value))