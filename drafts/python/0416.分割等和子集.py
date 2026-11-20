class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total, bits = sum(nums), 1
        for x in nums:
            bits |= bits << x
        return total % 2 == 0 and (bits >> (total // 2)) & 1 == 1
