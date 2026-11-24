prev = head

while prev.next is not None and prev.next.next:
    first = prev.next
    second = first.next
    first.next = second.next
    second.next = first
    prev.next = first
    prev = first
