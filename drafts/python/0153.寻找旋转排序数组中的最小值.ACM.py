n = int(input())
nums = list(map(int,input().split()))

l = 0
r = n - 1

while left < right:
    mid = (l + r)//2
    if nums[mid] < nums[l]:
        r = mid
    else:
        l = mid + 1

print(nums[r])
