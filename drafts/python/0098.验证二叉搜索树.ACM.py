from collections import deque
class TreeNode:
    def __init__(self,val = 0,left = None,right = None):
        self.val = val 
        self.left = left
        self.right = right

def check(node,low,high):
    if node is None:
        return True
    if node.val < low or node.val > high:
        return False
    return check(node.left,low,node.val) and check(node.right,node.val,high)

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
            queue.append(leftnode)
            node.left = leftnode
        if rightvalue != "null":
            rightnode = TreeNode(int(rightvalue))
            queue.append(rightnode)
            node.right = rightnode

print(check(root,float("-inf"),float("inf")))
