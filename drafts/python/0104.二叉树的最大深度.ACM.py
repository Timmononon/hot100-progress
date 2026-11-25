def depth(node):
    if node is None:
        return 0
    return max(depth(node.left),depth(node.right))+1
