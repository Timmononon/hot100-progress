s = input()
n = len(s)

path = []
res = []

def check(left,right):
    while left<right:
        if s[left] != s[right]:
            return False
        left +=1
        right -=1
    return True

def dfs(start):
    if start == n:
        res.append(path[:])
        return

    for end in range(start,n):
        if check(start,end):
            path.append(s[start:end+1])
