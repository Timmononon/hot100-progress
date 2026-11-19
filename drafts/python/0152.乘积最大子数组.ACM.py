n = int(input())
nums = list(map(int,input().split()))

low = nums[0]
high = nums[0]
best = nums[0]
for i in range(1,n):
    x = nums[i]
    if x < 0:
        low ,high = high , low

    high = max(x, high*x)
    low = min(x, low*x)

    best = max(best,high,low)

print(best)
