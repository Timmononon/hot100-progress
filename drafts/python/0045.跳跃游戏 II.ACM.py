n = int(input())
nums = list(map(int,input().split()))
far = 0
left = 0
right = 0
step=0
while right<n-1:
    for i in range(left,right+1):
        far = max(far,i+nums[i])

    left = right+1
    right = far
    step+=1
print(step)
