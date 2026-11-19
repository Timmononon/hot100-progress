s = input()

stack = []
k = 0
cur = ""
for ch in s:

    if ch.isdigit():
        k = k*10 + int(ch)
    elif ch =="[":
        stack.append((cur,k))
        cur = ""
        k = 0
    elif ch =="]":
        prev,times = stack.pop()
        cur = prev + cur * times
    else:
        cur += ch

print(cur)
