count = 0
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
for x1 in numbers:
    for x2 in numbers:
        for x3 in numbers:
            for x4 in numbers:
                if (x1 % 2 != 0 and x2 % 2 == 0) or (x1 % 2 == 0 and x2 % 2 != 0):
                    if (x3 % 2 != 0 and x4 % 2 == 0) or (x3 % 2 == 0 and x4 % 2 != 0):
                        count += 1
print(count)
