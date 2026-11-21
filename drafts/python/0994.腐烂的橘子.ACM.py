from collection import deque
r = int(input())
matrix = []
for _ in range(r):
    n = int(input())
    row = list(map(int,input().split()))
    matrix.append(row)
n = len(matrix[0])
queue = deque()
fresh = 0
for i in range(m):
    for j in range(n):
        if matrix[i][j] == 2:
            queue.append((i,j))
        elif matrix[i][j] == 1:
            fresh += 1
