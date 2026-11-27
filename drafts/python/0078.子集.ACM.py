n = int(input())
nums = list(map(int,input().split()))

res = []
path = []
def dfs(start):
    res.append(path[:])

    for i in range(start,n):
        path.append(nums[i])

        dfs(i+1)

        path.pop()
dfs(0)
print(len(res))

for i in range(len(res)):
    print(len(res[i]))
    if len(res[i]) !=0:
        print(*res[i])
