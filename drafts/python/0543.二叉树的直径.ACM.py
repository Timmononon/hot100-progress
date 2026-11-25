def fun(node):
    if node is None:
        return 0,0
    ldepth,lwidth = fun(node.left)
    rdepth,rwidth = fun(node.right)
