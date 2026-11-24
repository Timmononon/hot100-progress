class ListNode:
    def __init__(self,val = 0,next = None):
        self.val = val
        self.next = next

def merge_sort(node):
    if node is None or node.next is None:
        return node
    slow = node
    fast = node.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    r = slow.next
    slow.next = None

    left = merge_sort(node)
    right = merge_sort(r)

    head = ListNode()
    tail = head
    while left and right:
        if left.val <= right.val:
            tail.next = left
            left = left.next
        else:
            tail.next = right
            right = right.next
        tail = tail.next
    if left:
        tail.next = left
    else:
        tail.next = right
    return head.next
    
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
print(len(res))
print(*res)
