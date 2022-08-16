size = int(input())
if size == 1: print(1)
elif size < 4: print("NO SOLUTION")
else:
    for i in range(2, size + 1, 2):
        print(str(i), end=' ')
    for i in range(1, size + 1, 2):
        print(str(i), end=' ')