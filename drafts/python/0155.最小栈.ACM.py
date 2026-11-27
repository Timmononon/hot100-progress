n = int(input())

stack = []
min_stack =[]

for _ in range(n):
    parts = input().split()
    key = parts[0]

    if key == "PUT":
        val = int(parts[1])
        stack.append(val)

        if not min_stack:
            min_stack.append(val)
        else:
            min_stack.append(min(val,min_stack[1]))

    elif key == "POP":
        stack.pop()
        min_stack.pop()
