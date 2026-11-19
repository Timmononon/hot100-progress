n = int(input())
nums = list(map(int,input().split()))

left = 0
right = n - 1
res = 0
while left < right:
    if nums[right] < nums[left]:
        res+=1
        right -=1
    else:
