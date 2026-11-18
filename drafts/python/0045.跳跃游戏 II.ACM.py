n = int(input())
nums = list(map(int,input().split()))

left = 0
right = 0
jump = 0
far = 0
while right < n - 1:
    if i in range(left,right + 1):
        far = max(far , i + nums[i])
    left = right + 1
    right = far
    jump += 1
print(jump)
