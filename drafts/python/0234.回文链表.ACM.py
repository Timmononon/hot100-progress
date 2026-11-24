class ListNode:
    def __init__(self,val = 0,next = None):
        self.val = val
        self.next = next
n = int(input())
nums = list(map(int,input().split()))

head = ListNode()
tail = head

for x in nums:
    node = ListNode(x)
    tail.next = node
    tail = node
head = head.next

fast = head
slow = head
while fast and fast.next:
    slow = slow.next
    fast = fast.next.next
prev = None
while slow:
    nextnode = slow.next
    slow.next = prev
    prev = slow
    slow = nextnode
