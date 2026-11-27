n = int(input())
nums = list(map(int,input().split()))

stack = []
res = [0] * n

for i in range(n):
    while stack and nums[i] > nums[stack[-1]]:
        prev = stack.pop()
        res[prev] = i - prev

    stack.append(i)

print(len(res))
print(*res)
