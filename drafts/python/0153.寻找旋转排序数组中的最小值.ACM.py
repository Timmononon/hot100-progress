n = int(input())
nums = list(map(int, input().split()))

l = 0
r = n - 1

while l < r:
    mid = (l+r)//2
