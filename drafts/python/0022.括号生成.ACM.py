n = int(input())
path = []

def dfs(left,right):
    if len(path) == 2*n:
        print("".join(path))

    if left < n:
        path.append("(")
        dfs(left+1,right)
        path.pop()
    if right<left:
        path.append(")")
        dfs(left,right+1)
        path.pop()

dfs(0,0)
