# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder: return None
        root = TreeNode(preorder[0]) #First element of preorder is the root
        mid = inorder.index(preorder[0]) #Inorder gives you whats at the left and right of the root.
        root.left = self.buildTree(preorder[1: mid+1], inorder[:mid])
        root.right = self.buildTree(preorder[mid+1: ], inorder[mid+1:])
        return root
