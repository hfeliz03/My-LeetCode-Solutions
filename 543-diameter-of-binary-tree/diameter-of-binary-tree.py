# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        #Create a global variable in which we store the current max diameter
        self.maxDiam = 0
        if root is None:
            return 0
        else:
            #Call the diameter helper recursively, the maxDiam will get updated automatically -
            #if needed, then returned
            self.diameterOfBinaryTreeHelper(root)
            return self.maxDiam
    
    def diameterOfBinaryTreeHelper(self, root) -> int:
        #If we are past a leaf node, stop recurring
        if root is None: 
            return 0
        else: 
            #Find the depths of the subtree to the left and to the right
            leftDepth = self.diameterOfBinaryTreeHelper(root.left)
            rightDepth = self.diameterOfBinaryTreeHelper(root.right)
            #Compare if at the given root the diameter is bigger than the current max
            self.maxDiam = max(leftDepth+rightDepth, self.maxDiam)
            return 1 + max(leftDepth, rightDepth)