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
