n = int(input())
nums = list(map(int,input().split()))

far = 0
flag = True
for i in range(n):

    if i>far:
        flag = False
        break

    far = max(far,i+nums[i])

print(flag)
