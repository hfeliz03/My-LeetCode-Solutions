# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        MOD = 10**9 + 7

        def total_sum(node: Optional[TreeNode]) -> int:
            if not node: return 0
            return node.val + total_sum(node.left) + total_sum(node.right) # Cur val + go left + go right

        total = total_sum(root)
        best = float("-inf")

        def dfs(node: Optional[TreeNode]) -> int:
            nonlocal best
            if not node: return 0

            s = node.val + dfs(node.left) + dfs(node.right)   # subtree sum at node

            best = max(best, s * (total - s)) # if we cut above this subtree, product is:

            return s

        dfs(root)
        return best % MOD