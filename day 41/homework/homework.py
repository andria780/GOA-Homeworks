random_numbers = [10, 15, 20, 30, 35, 12, 13, 14, 15, 16]
total = 0
for i in random_numbers:
    if i %5 == 0:
        total += i
print(total)