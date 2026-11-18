s = input()
p = input()

need = [0] * 26
window = [0] * 26
base = ord('a')

for str in p:
    need[ord(str)-base] += 1

left = 0
res = []
for right in range(len(s)):

    window[ord(s[right])-base] += 1

    if (right-left+1) > len(p):
        window[ord(s[left])-base] -= 1
        left += 1
    if right-left +1 == len(p) and window == need:
        res.append(left)
print(len(res))
print(*res)
