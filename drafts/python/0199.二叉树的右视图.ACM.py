from collections import deque
class TreeNode:
    def __init__(self,val = 0,left = None,right = None):
        self.val = val
        self.left = left
        self.right = right
n = int(input())
nums = input().split()
tokens = iter(nums)
rootvalue = next(tokens,"null")
root = None
queue = deque()
if rootvalue !="null":
    root = TreeNode(int(rootvalue))
    queue.append(root)

    leftvalue = next(tokens,"null")
    rightvalue = next(tokens,"null")
