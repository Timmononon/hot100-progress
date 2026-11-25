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

    while queue:
        node = queue.popleft()
        leftvalue = next(tokens,"null")
        rightvalue = next(tokens,"null")
        
        if leftvalue !="null":
            leftnode = TreeNode(int(leftvalue))
            node.left = leftnode
            queue.append(leftnode)
        if rightvalue !="null":
            rightnode = TreeNode(int(rightvalue))
            node.right = rightnode
            queue.append(rightnode)

queue = deque()
if root:
    queue.append(root)

while queue:

    size = len(queue)

    for i in range(size):
        node = queue.popleft()
