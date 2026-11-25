from collections import deque
class TreeNode:
    def __init__(self,val = 0,left = None,right = None):
        self.val = val
        self.left = left
        self.right = right
def rev(node):
    if node is None:
        return
    node.left ,node.right = node.right,node.left
    rev(node.left)
    rev(node.right)


n = int(input())
nums = input().split()
tokens = iter(nums)
rootvalue = next(tokens,"null")
queue = deque()
root = None

if(rootvalue != "null"):

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

rev(root)
res = []
queue = deque()
queue.append(root)
while queue:
    node = queue.popleft()
    if node is None:
        res.append("null")
    else:
        res.append(node.val)
        queue.append(node.left)
        queue.append(node.right)

while res and res[-1] == "null":
    res.pop()
print(len(res))
print(*res)
