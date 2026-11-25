def check(node):
    if node is None or node.val == p or node.val == q:
        return node

    left = check(node.left)
    right = check(node.right)

    if left and right:
        return node
    if left:
        return left
    return right
