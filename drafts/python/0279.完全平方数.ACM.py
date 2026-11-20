n = int(input())

dp = [float("inf")] * (n+1)
base = 1
dp[0] = 0
while base * base <= n:
    sq = base * base
    for i in range(sq,n+1):
        dp[i] = min(dp[i],dp[i-sq]+1)

    base+=1

print(dp[n])
