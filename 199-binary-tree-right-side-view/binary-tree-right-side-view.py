# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # Keep iterating
        res = []
        def traverse(node, level):
            nonlocal res
            if not node: return
            if level > len(res):
                res.append(node.val)
            traverse(node.right, level+1)
            traverse(node.left, level+1)
        
        traverse(root, 1)
        return res

