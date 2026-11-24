prev = head
while prev.next and prev.next.next:
    first = prev.next
    second = prev.next
    first.next = second.next
    second.next = first
    prev.next = second
    prev = first
