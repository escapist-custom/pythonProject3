price = int(input("Введите цену: "))
summ = 0

while price != 0:
    if price > 1000:
        summ += (price * 0.95)
    else:
        summ += price
    price = int(input("Введите цену: "))
print(round(summ, 2))