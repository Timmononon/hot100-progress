n = int(input())
nums = list(map(int, input().split()))

left = 0
i = 0
right = n - 1

while i <= right:
    if nums[i] == 0:
        nums[left], nums[i] = nums[i], nums[left]
        left += 1
        i += 1

    elif nums[i] == 1:
        i += 1

    else:
        nums[i], nums[right] = nums[right], nums[i]
        right -= 1

print(*nums)
