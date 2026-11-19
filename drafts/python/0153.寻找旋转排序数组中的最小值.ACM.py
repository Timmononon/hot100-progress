n = int(input())
nums = list(map(int, input().split()))

l = 0
r = n - 1

while l < r:
    mid = (l + r) // 2

    if nums[mid] > nums[r]:
        l = mid + 1
    else:
        r = mid

print(nums[l])
