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
