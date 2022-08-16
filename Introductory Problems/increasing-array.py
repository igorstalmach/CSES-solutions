size = int(input())
nums = list(map(int, input().split()))
it = 0
for i in range(size-1):
    if nums[i] > nums[i+1]:
        it += nums[i] - nums[i+1]
        nums[i+1] = nums[i]
print(it)