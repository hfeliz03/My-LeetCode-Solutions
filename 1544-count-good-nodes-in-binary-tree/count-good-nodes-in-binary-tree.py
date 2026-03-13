# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        #We will be doing dfs most likely because we want to check for x if X is the greater node ever seen on Xs path
        #keep the maximum at a given path, if X is smaller than its path max then X wont be good
        #Keep a global variable with the length of the tree, once you see a non-good tree, decrease it
        def getLen(node):
            if not node:
                return 0
            else: 
                return 1 + getLen(node.left) + getLen(node.right)
        
        good = getLen(root)

        def dfs(node, maxInPath):
            nonlocal good
            if not node: return 
            else:
                if node.val < maxInPath:
                    good -= 1
                maxInPath = max(node.val, maxInPath)
                dfs(node.left, maxInPath)
                dfs(node.right, maxInPath)
            
        dfs(root, root.val)

        return good