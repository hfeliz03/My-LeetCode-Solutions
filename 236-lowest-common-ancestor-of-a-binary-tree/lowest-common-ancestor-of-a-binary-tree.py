# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def bottom(node):
            if not node: return None # Trivial
            
            if node == p or node == q: #Return that node that is a match
                return node
            
            l = bottom(node.left) #Go all the way to the left
            r = bottom(node.right) #Then go right
            
            if l and r:
                return node
            
            return l if l else r
        
        return bottom(root)