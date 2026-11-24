class ListNode:
    def __init__(self,val = 0,next = None,random = None):
        self.val = val
        self.next = next
        self.random = random

n = int(input())
nums = list(map(int,input().split()))
