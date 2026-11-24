m,n,target = map(int,input().split())
matrix = []
for _ in range(m):
    row = list(map(int,input().split()))
    matrix.append(row)
l = 0
r = m*n-1

while l<r:
    mid = (l+r)//2
