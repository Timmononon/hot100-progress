q = int(input())
s = input().split()
size = int(s[1])
cache = {}
for _ in range(q-1):
    parts = input().split()
    key = int(parts[1])
    if parts[0] == "get":
