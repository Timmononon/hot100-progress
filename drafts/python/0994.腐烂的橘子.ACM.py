from collections import deque
r = int(input())
matrix = []
for _ in range(r):
    n = int(input())
    row = list(map(int,input().split()))
    matrix.append(row)
n = len(matrix[0])
queue = deque()
