# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        #If the tree is empty, return None. If both children are None, we reached a leaf node
        if root is None or (root.left is None and root.right is None):
            return root

        #Temporary variable to hold reference to subtree being swapped
        temp = root.left

        #Inversion is performed
        root.left = root.right
        root.right = temp

        #Recursive Call
        self.invertTree(root.right)
        self.invertTree(root.left)

        #Return the root of each subtree once traversed all its children
        return root