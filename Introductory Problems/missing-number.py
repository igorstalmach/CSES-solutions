size = list(range(1,int(input())+1))
nsize = list(map(int, input().split()))
print(sum(size)-sum(nsize))