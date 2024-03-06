number = int(input())
numbers = list(map(int, input().split()))

result = numbers.copy()
for i in numbers:
    if i >= 0:
        result.remove(i)
print(max(result))
