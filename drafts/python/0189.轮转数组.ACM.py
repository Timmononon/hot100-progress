n,k = map(int,input().split())
nums = list(map(int,input().split()))

def rev(nums,left,right):

    while left<right:
        nums[left],nums[right] = nums[right],nums[left]

        left+=1
        right-=1

k = k%n

rev(nums,0,n-1)
rev(nums,0,k-1)
rev(nums,k,n-1)

print(*nums)
