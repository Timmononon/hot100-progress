s = input()
n = len(s)
end = 0
start = 0
last = {}
res = []
for i in range(n):
    last[s[i]] = i
for i in range(n):
    end = max(end,last[s[i]])

    if i == end:
        res.append(end-start+1)
        start=i+1

print(len(res))
print(*res)
