# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        nums = []
        def helper(root, s):
            if not root: return
            if not root.left and not root.right: 
                nums.append(s + str(root.val))
                return 
            else: 
                helper(root.left, s + str(root.val))
                helper(root.right, s + str(root.val))
                return 
        
        helper(root, "")

        print(nums)
        sumInt = 0
        for i in range(len(nums)):
            sumInt += int(nums[i],2)
        return  sumInt

        