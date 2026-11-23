n = int(input())
nums = list(map(int,input().split()))

nums = sorted(nums)
res = []
for i in range(n-2):
    left = i+1
    right = n-1
    while left < right:
        total = nums[i] + nums[left] + nums[right]

        if total < 0:
            left += 1
        elif total > 0:
            right -= 1
        else:
            res.append(nums[i],nums[left],nums[right])
            left += 1
            right -= 1

            while left<right and nums[left] == nums[left-1]:
                left+=1
            while left<right and nums[right]==nums[right+1]:
                right-=1
