# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        cur = root
        minVal, maxVal = min(p.val, q.val), max(p.val, q.val)
        while cur:
            if (cur.val >= minVal) and (cur.val <= maxVal):
                return cur
            elif cur.val > minVal and cur.val > maxVal: #CurNode is bigger than both, go to the left
                cur = cur.left
            else: ##CurNode is smaller than both, go to the right
                cur = cur.right
        return root