m = int(input())
n = int(input())
dp = []
for _ in range(m):
    row = [1] * n
    dp.append(row)

for i in range(1,m):
    for j in range(1,n):
        dp[i][j] = dp[i-1][j] + dp[i][j-1]
print(dp[m-1][n-1])
