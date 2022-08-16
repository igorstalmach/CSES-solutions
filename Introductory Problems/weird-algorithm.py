temp = int(input())
print(temp)
while temp != 1:
    temp = (int(temp/2), temp*3+1)[temp%2]
    print(temp)