# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None: return True
        return self.balanceHeight(root)[0]
    
    def balanceHeight(self, root: Optional[TreeNode]) :
        if root is None : return [True, 0]
        left, right = self.balanceHeight(root.left), self.balanceHeight(root.right)
        return  [(left[0] and right[0] and abs(left[1]-right[1]) <= 1) , 1+max(left[1], right[1]) ]
    
    