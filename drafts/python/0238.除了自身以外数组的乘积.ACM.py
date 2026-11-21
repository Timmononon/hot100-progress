n = int(input())
nums = list(map(int,input().split()))

res = [1] * n 
left = 1
for i in range(n):
    res[i] = left
    left *= nums[i]
right = 1
for i in range(n-1,-1,-1):
    res[i] * right
    right *=nums[i]

print(*res)
