n = int(input())
seen = {}
for _ in range(n):
    word = input()
    key = "".join(sorted(word))
    if key not in seen:
        seen[key] = []
    seen[key].append(word)

print(len(seen))
for v in seen.values():
    print(len(v))
    for word in v:
        print(word)
