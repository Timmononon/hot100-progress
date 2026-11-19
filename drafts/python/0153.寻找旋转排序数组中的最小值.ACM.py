n = int(input())
nums = list(map(int,input().split()))

left = 0
right = n - 1
res = nums[0]
while left < right:
    if nums[right] < nums[left]:
        res = nums[right]
        right -=1
    else:
        break
print(res)
