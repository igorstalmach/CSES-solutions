a = input()
ls = sorted(list(set(a)))
it = 0
out = ''
temp = ''
for i in ls:
    n = a.count(i)
    if n % 2 == 0:
        temp += i * (n//2)
    elif it==1:
        temp = 0
        print("NO SOLUTION")
        break
    else:
        it = 1
        out = i
        temp += i * ((n-1)//2)
if temp != 0:
    print(temp + out + temp[::-1])