n = int(input())
sum = (n*(n+1))//2
if sum % 2 == 0:
    sum1 = []
    sum2 = []
    tsum = sum // 2
    for i in reversed(range(1,n+1)):
        if tsum - i >= 0:
            tsum -= i
            sum1.append(i)
        else:
            sum2.append(i)

    print("YES")
    print(len(sum1))
    print(' '.join(list(map(str, sum1))))
    print(len(sum2))
    print(' '.join(list(map(str, sum2))))
else:
    print("NO")