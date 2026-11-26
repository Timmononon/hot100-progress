n = int(input())
nums = list(map(int,input().split()))

count = 0
candidate = None

for num in nums:
    if count ==0:
        candidate  =num
    if candidate == num:
        count+=1
    else:
        count-=1
print(candidate)
