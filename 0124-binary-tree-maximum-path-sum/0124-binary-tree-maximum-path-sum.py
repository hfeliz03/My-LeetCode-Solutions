# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        #Get all the way down to the leaf node
        #If leaf, then just push up that value
        #if non leaf, get max(left, right, left+right) and add current val, push up
        maxSum = root.val
        def traverse(node):
            nonlocal maxSum
            if (not node): return 0
            if not node.left and not node.right: #Leaf node
                maxSum = max(node.val, maxSum) #Max could be the leaf by itself
                return node.val
            l, r = traverse(node.left), traverse(node.right)
            curMax = max(l, r, l+r, 0) + node.val
            maxSum = max(curMax, maxSum)
            return max(l, r, 0) + node.val

        traverse(root)
        return maxSum