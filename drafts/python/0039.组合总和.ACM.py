n,target = map(int,input().split())
nums = list(map(int,input().split()))

res = []
path = []
def dfs(start,remain):
    if remain == 0:
        res.append(path[:])
        return
    for i in range(start,n):
        if nums[i] > remain:
            break
        path.append(nums[i])

        dfs(i,remain - nums[i])

        path.pop()
dfs(0,target)
print(len(res))

for i in range(len(res)):
    print(*res[i])
