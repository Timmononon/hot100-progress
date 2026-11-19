n = int(input())
nums = list(map(int, input().split()))

l = 0
r = n - 1
last = nums[n-1]
while l < r:
    mid = (l+r)//2
    if nums[mid] <= last:
        r = mid
    else:
        l = mid + 1
print(nums[l])
