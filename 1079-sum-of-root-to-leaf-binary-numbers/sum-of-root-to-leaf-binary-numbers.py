# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        
        def helper(root, s):
            nonlocal sumInt
            if not root: 
                return
            if not root.left and not root.right: 
                sumInt += int(s + str(root.val),2)
                return 
            else: 
                helper(root.left, s + str(root.val))
                helper(root.right, s + str(root.val))
                return 
        
        sumInt = 0
        helper(root, "")

        return  sumInt

        