m = int(input())
matrix = []
for _ in range(m):
    n = int(input())
    row = list(map(int,input().split()))
    matrix.append(row)
dp = []
for _ in range(m):
    row = [0]*n
    dp.append(row)

dp[0][0] = matrix[0][0]

for i in range(m):
    for j in range(n):
        if i==0 and j ==0:
            continue
        elif i == 0:
            dp[i][j] = dp[i][j-1]+matrix[i][j]
        elif j == 0:
            dp[i][j] = dp[i-1][j]+matrix[i][j]
        else:
            dp[i][j] = min(dp[i-1][j],dp[i][j-1]) + matrix[i][j]

print(dp[m-1][n-1])
