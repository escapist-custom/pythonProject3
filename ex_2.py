list_numbers = []

number = int(input())
while number != 0:
    list_numbers.append(number)
    number = int(input())
print(sorted(list_numbers))