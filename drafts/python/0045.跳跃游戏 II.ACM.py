n = int(input())
nums = list(map(int,input().split()))
res = 0
i = 0
while i<n: 
    far = 0
    while far < nums[i]:
        if nums[i+far] > (nums[i] - far):
            i = i+far
            res +=1
            break
        far +=1
    i = i+far
    res+=1

print(res)
