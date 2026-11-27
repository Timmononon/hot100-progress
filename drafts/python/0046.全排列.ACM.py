n = int(input())
nums = list(map(int,input().split()))

used = [False] * n
path = []
res = []
def dfs():
    if len(path) == n:
        res.append(path[:])
        return

    for i in range(n):
        if used[i]:
            continue

        path.append(nums[i])
        used[i] = True

        dfs()

        path.pop()
        used[i] = False
dfs()
print(len(res))
for x in res:
    print(len(x))
    print(*x)
