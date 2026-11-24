p = head1
q = head2
if p is not q:
    if p is None:
        p = head2
    else:
        p = p.next
    if q is None:
        q = head1
    else:
        q = q.next

if p is None:
    print(-1)
else:
    print(p)
