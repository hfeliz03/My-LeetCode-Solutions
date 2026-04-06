# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def helper(node, curVal):
            if not node: return False

            curVal += node.val

            if not node.left and not node.right: return curVal == targetSum

            return helper(node.left, curVal) or helper(node.right, curVal)
        return helper(root, 0) if root else False