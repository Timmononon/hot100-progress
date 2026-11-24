n = int(input())
nums = list(map(int,input().split()))

def quick_sort(q,l,r):
    if l>=r:
        return
    i = l-1
    j = r+1
    x = q[l]

    while i<j:
        i+=1
        while q[i]<x:
            i+=1
        j-=1
        while q[j]>x:
            j-=1
        if i<j:
            q[i],q[j] = q[j],q[i]
        quick_sort(q,l,j)
        quick_sort(q,j+1,r)
