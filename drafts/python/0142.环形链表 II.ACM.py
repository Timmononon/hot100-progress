class ListNode:
    def __init__(self,val = 0,next = None):
        self.val = val
        self.next = next

n = int(input())
nums = list(map(int,input().split()))
pos = int(input())

head = ListNode()
tail = head
position = None
for i in range(n):
    num = nums[i]
    node = ListNode(num)
    tail.next = node
    tail = node

    if i==pos:
        position = node

if position is not None:
    tail.next = position

head = head.next
slow = head
fast = head
meet = None
while fast and fast.next:
    slow = slow.next
    fast = fast.next.next

    if slow is fast:
        meet = slow
        break
index = 0
if meet is None:
    print(-1)
else:
    p = head
    q = meet

    while p is not q:
        p = p.next
        q = q.next
        index +=1
    print(index)
