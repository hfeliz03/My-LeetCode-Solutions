# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []

        stack = [(root, False)]  # (node, visited)
        res = []

        while stack:
            node, visited = stack.pop()
            if node:
                if visited: res.append(node.val)
                else:
                    # Postorder: Left -> Right -> Node
                    stack.append((node, True))
                    stack.append((node.right, False))
                    stack.append((node.left, False))
        
        return res