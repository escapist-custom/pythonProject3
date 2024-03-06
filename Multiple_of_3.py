num1 = int(input("Введите первое число диапазона: "))
num2 = int(input("Введите второе число диапазона: "))

while num1 <= num2:
    if num1 % 3 == 0:
        print(num1)
    num1 += 1
