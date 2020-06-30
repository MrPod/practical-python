# bounce.py
#
# Exercise 1.5
i = 0
height = 100

while i < 10:
    i += 1
    height *= 3 / 5
    print(i, round(height, 4))