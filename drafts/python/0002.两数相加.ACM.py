class ListNode:
    def __init__(self,val = 0,next = None):
        self.val =val
        self.next = next

def build(nums):
    head = ListNode()
    tail = head

    for x in nums:
        node = ListNode(x)
        tail.next = node
        tail = node

    return head.next

n = int(input())
nums1 = list(map(int,input().split()))
m = int(input())
nums2 = list(map(int,input().split()))

head1 = build(nums1)
head2 = build(nums2)

p = head1
q = head2

head = ListNode()
tail = head
carry = 0
while p or q or carry:
    x = 0
    y = 0
    if p:
        x = p.val
        p = p.next
    if q:
        y = q.val
        q = q.next
    total = x+y+carry

    digit = total%10
    carry = total//10
    node = ListNode(digit)
    tail.next = node
    tail = node

head = head.next
res = []
while head:
    res.append(head.val)
    head = head.next
print(len(res))
print(*res)
