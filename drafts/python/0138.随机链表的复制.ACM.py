class ListNode:
    def __init__(self,val = 0,next = None,random = None):
        self.val =val
        self.next = next
        self.random = random

def copy(head):


n = int(input())
head = ListNode()
tail = head
nodes = []
indices = []
for _ in range(n):
    value,index = map(int,input().split())
    node = ListNode(value)
    tail.next = node
    tail = node
