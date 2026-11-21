s = input()
n = len(s)

path = []
res = []

def check(left,right):
    while left<right:
        if s[left] != s[right]:
            return False
        left +=1
        right -=1
    return True
