for _ in range(int(input())):
    n1, n2 = input().split()
    n1, n2 = int(n1), int(n2)
    if max(n1,n2) > 2 * min(n1,n2):
        print("NO")
    elif (n1 + n2) % 3 == 0:
        print("YES")
    else:
        print("NO")