n = int(input())
nums = list(map(int, input().split()))

jumps = 0
low = 0
high = 0

while high < n - 1:
    farthest = high

    for i in range(low, high + 1):
        farthest = max(farthest, i + nums[i])

    low = high + 1
    high = farthest
    jumps += 1

print(jumps)
