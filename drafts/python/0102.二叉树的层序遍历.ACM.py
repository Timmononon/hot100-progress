queue = deque()
if root:
    queue.append(root)

while queue:
    level = []
    size = len(queue)

    for _ in range(size):
        node = queue.popleft()
        level.append(node.val)

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    print(*level)
