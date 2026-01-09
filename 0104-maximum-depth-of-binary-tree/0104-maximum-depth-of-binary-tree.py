# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        maxDepth = 0
        def dfs(root, depth):
            if(not root):
                print("leaf")
                nonlocal maxDepth 
                maxDepth = max(maxDepth, depth)
                return
            print(root.val)
            dfs(root.left, depth+1)
            dfs(root.right, depth+1)
        
        dfs(root, 0)
        return maxDepth