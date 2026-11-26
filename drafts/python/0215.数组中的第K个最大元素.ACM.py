import heapq
n = int(input())
nums = list(map(int,input().split()))
k = int(input())

heap = []
for num in nums:
    heapq.heappush(heap,num)

    if len(heap)>k:
        heapq.heappop(heap)

print(heap[0])
