n = int(input())
matrix = []
for _ in range(n):
    n = int(input())
    row = list(map(int,input().split()))
    matrix.append(row)

for i in range(n):
    for j in range(i+1,n):
        matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]

for row in matrix:
    row.reverse()

print(n)
for row in matrix:
    print(len(row))
    print(*row)
