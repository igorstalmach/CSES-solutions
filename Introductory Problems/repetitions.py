data = list(input())
longest = 0
temp = 1
for a in range(len(data)):
    try:
        if data[a] == data[a+1]:
            temp += 1;
        else:
            if temp > longest:
                longest = temp
            temp = 1
    except IndexError:
        if temp > longest:
                longest = temp
print(longest)