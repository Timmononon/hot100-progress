head = Listnode()
tail = head

while head1 is not None and head2 is not None:
    if head1.val<=head2.val:
        tail.next = head1
        head1 = head1.next
    else:
        tail.next = head2
        head2 = head.next
    tail = tail.next

if head1 is not None:
    tail.next = head1
else:
    tail.next = head2
