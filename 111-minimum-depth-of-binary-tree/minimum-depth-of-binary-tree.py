# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0

        if not root.left and not root.right: return 1

        if not root.left:
            return 1 + self.minDepth(root.right)

        if not root.right:
            return 1 + self.minDepth(root.left)

        return 1 + min(self.minDepth(root.left), self.minDepth(root.right))
        # if not root: return 0
        # minDepth = 10**5
        # def dfs(root, level):
        #     nonlocal minDepth
        #     if not root.left and not root.right:
        #         minDepth = min(level, minDepth)
        #         return
        #     print(root.val)
        #     if root.left : dfs(root.left, level+1)
        #     if root.right :dfs(root.right, level+1)

        # dfs(root, 1) 
        # return minDepth