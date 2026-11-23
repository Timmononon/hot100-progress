n = int(input())
seen = {}
for _ in range(n):
    word = input()
    key = "".join(sorted(word))
    if key not in seen:
        seen[key] = []
    seen[key].append(word)

print(len(seen))
res = []
for v in seen.values():
    res.append(v)
    print(len(res))
    for r in res:
        print(r)
    res = []
