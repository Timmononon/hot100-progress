from collections import deque
class TreeNode:
    def __init__(self,val = 0,left = None,right = None):
        self.val = val
        self.left = left
        self.right = right

def dfs(node):
    if node is None:
        return 0,0

    leftdepth,leftwith = dfs(node.left)
    rightdepth,rightwith = dfs(node.right)

    depth = max(leftdepth,rightdepth)+1
    width = max(leftwith,rightwith,leftdepth+rightdepth)

    return depth,width

n = int(input())
nums = input().split()
tokens = iter(nums)
rootvalue = next(tokens,"null")
root = None
queue = deque()

if rootvalue != "null":

    root = TreeNode(int(rootvalue))
    queue.append(root)

    while queue:

        node = queue.popleft()

        leftvalue = next(tokens,"null")
        rightvalue = next(tokens,"null")

        if leftvalue != "null":
            leftnode = TreeNode(int(leftvalue))
            node.left = leftnode
            queue.append(leftnode)
        if rightvalue != "null":
            rightnode = TreeNode(int(rightvalue))
            node.right = rightnode
            queue.append(rightnode)

depth,width = dfs(root)
print(width)
