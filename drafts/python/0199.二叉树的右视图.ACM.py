class TreeNode:
    def __init__(self,val = 0,left = None,right = None):
        self.val = val
        self.left = left
        self.right = right
n = int(input())
nums = input().split()
tokens = iter(nums)
rootvalue = next(tokens)
