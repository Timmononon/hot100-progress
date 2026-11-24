m,n = map(int,input().split())
matrix = []

for _ in range(m):
    row = list(map(int,input().split()))
    matrix.append(row)
row = set()
col = set()

for i in range(m):
    for j in range(n):
        if matrix[i][j] == 0:
            row.add(i)
            col.add(j)

for i in range(m):
    for j in range(n):
        if i in row or j in col:
            matrix[i][j] = 0
