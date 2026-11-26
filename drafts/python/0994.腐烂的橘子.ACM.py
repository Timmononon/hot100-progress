from collections import deque
r = int(input())
matrix = []
for _ in range(r):
    n = int(input())
    row = list(map(int,input().split()))
    matrix.append(row)
n = len(matrix[0])
queue = deque()
fresh = 0
for i in range(r):
    for j in range(n):
        if matrix[i][j] == 2:
            queue.append((i,j))
        elif matrix[i][j] ==1:
            fresh+=1

directions = [(-1,0),(1,0),(0,1),(0,-1)]
time = 0
while queue and fresh!=0:
    size = len(queue)
    for _ in range(size):
        i,j = queue.popleft()
        for di,dj in directions:
            ni = di+i
            nj = dj+j
            if 0<=ni<r and 0<=nj<n and matrix[ni][nj] == 1:
                matrix[ni][nj] =2
                queue.append((ni,nj))
                fresh-=1
    time+=1

if fresh == 0:
    print(time)
else:
    print(-1)
