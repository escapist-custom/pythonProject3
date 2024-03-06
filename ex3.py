n = int(input())
k = int(input())
lst_boring = []

for i in range(1, n):
    num = ""
    for j in str(i):
        num += j
    if len(set(num)) == 1:
        lst_boring.append(i)
if k in lst_boring:
    print()
