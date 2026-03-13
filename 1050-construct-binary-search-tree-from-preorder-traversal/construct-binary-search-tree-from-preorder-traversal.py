# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]: 

        self.i = 0

        def preOrderTree(bound=float("inf")):
            if self.i >= len(preorder) or preorder[self.i] > bound: return None

            root = TreeNode(preorder[self.i])
            self.i += 1
            
            root.left = preOrderTree(root.val)
            root.right = preOrderTree(bound)

            return root

        
        return preOrderTree()