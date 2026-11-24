s = input()
n = len(s)
right = 0
left = 0
res = 0
seen = set()
for right in range(n):
    ch = s[right]
    while ch in seen:
        seen.remove(s[left])
        left+=1
    seen.add(ch)
    res = max(res,len(seen))
print(res)
