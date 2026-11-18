n = int(input())
nums = list(map(int,input().split()))

i = 0
while i<n: 
    far = 0
    while far < nums[i]:
        if nums[i+far] > (nums[i] - far):
