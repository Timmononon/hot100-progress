n = int(input())
nums = list(map(int,input().split()))

lowest = float("inf")
res = 0
for num in nums:
    lowest = min(lowest,num)
    res = max(res,num-lowest)
print(res)
