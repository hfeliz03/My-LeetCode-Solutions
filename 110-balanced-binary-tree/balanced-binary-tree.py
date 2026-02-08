# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.res = True
        
        def isBalancedHelper(root):
            if not root:
                return 0
            
            h1 = isBalancedHelper(root.left)
            h2 = isBalancedHelper(root.right)
            if abs( h1 - h2 ) > 1: 
                self.res = False
            return max(h1,h2) + 1

        isBalancedHelper(root)

        return self.res
       