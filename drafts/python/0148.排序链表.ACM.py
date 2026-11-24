class ListNode:
    def __init__(self,val = 0,next = None):
        self.val = val
        self.next = next

def merge_sort(node):

n = int(input())
nums = list(map(int , input().split()))

head = ListNode()
tail = head
for x in nums:
    node = ListNode(x)
    tail.next = node
    tail = node

head = head.next
head = merge_sort(head)
res = []
while head is not None:
    res.append(head.val)
    head = head.next
print(*res)
