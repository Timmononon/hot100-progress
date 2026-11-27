m,n = map(int,input().split())
matrix = []
for _ in range(m):
    s = input().split()
    matrix.append(s)
word = input()

def dfs(i,j,k):
    if i<0 or i>=m or j<0 or j>=n:
        return False
    if matrix[i][j] != word[k]:
        return False
    if k == len(word) - 1:
        return True

    letter = matrix[i][j]
    matrix[i][j] = "#"

    found = (
        dfs(i-1,j,k+1) or 
        dfs(i+1,j,k+1) or
        dfs(i,j-1,k+1) or
        dfs(i,j+1,k+1)
    )

    matrix[i][j] = letter

    return found


def exist():
    for i in range(m):
        for j in range(n):
            if dfs(i,j,0):
                return True
    return False
print(exist())
