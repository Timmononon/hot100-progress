m,n,target = map(int,input().split())
matrix = []
for _ in range(m):
    row = list(map(int,input().split()))
    matrix.append(row)
l = 0
r = m*n-1

while l<r:
    mid = (l+r)//2
    row = mid//n
    col = mid%n
    if matrix[row][col]>=target:
        r = mid
    else:
        l = mid+1
row = l//n
col = l%n

if matrix[row][col] == target:
    print(True)
else:
    print(False)
