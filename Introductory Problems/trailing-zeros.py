def trail(n):
    sum = 0
    while(n >= 5):
        n //= 5
        sum += n
    return sum
print(trail(int(input())))