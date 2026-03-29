# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        lca = root
        cur = root
        minVal = min(p.val, q.val)
        maxVal = max(p.val, q.val)
        while cur:
            if (cur.val >= minVal) and (cur.val <= maxVal):
                lca = cur
                break
            elif cur.val > minVal and cur.val > maxVal: #CurNode is bigger than both, go to the left
                cur = cur.left
            elif cur.val < p.val and cur.val < q.val: ##CurNode is smaller than both, go to the right
                cur = cur.right
        return lca