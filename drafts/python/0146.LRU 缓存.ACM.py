class ListNode:
    def __init__(self,key = 0,val = 0,next = None,prev = None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev
def remove(node):
    node.next.prev = node.prev
    node.prev.next = node.next

def addfront(node):
    node.prev = head
    node.next = head.next
    node.next.prev = node
    head.next = node

head = ListNode()
tail = ListNode()
head.next = tail
tail.prev = head

q = int(input())
s = input().split()
size = int(s[1])
print("null")
cache = {}
for _ in range(q-1):
    parts = input().split()
    key = int(parts[1])
    if parts[0] == "get":
        if key not in cache:
            print(-1)
        else:
            node = cache[key]
            print(node.val)
            remove(node)
            addfront(node)

    if parts[0] == "put":
        value = parts[2]
        print("null")
        if key in cache:
            node = cache[key]
            node.val = value
            remove(node)
        else:
            node = ListNode(key,value)
            cache[key] = node
            
        addfront(node)
        if len(cache) > size:
            node = tail.prev
            remove(node)
            del cache[node.key]
