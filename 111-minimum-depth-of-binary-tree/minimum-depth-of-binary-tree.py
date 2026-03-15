# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        minDepth = 10**5
        def dfs(root, level):
            nonlocal minDepth
            if not root.left and not root.right:
                minDepth = min(level, minDepth)
                return
            print(root.val)
            if root.left : dfs(root.left, level+1)
            if root.right :dfs(root.right, level+1)

        if root: dfs(root, 1) 
        else: minDepth = 0
        return minDepth