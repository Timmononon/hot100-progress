import heapq
n = int(input())
nums = list(map(int,input().split()))
k = int(input())
counts = {}
for num in nums:
    counts[num] = counts.get(num,0)+1

heap = []
for key,value in counts.items():
    heapq.heappush(heap,(value,key))

    if len(heap)>k:
        heapq.heappop(heap)

res= []
while heap:
    key,value = heapq.heappop(heap)
    res.append(value)
print(len(res))
print(*res)
