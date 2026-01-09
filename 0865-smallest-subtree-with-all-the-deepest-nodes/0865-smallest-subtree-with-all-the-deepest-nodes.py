# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node):
            if not node: return (None, 0)   # (subtree_root, depth)
            
            left_node, left_depth = dfs(node.left)
            right_node, right_depth = dfs(node.right)
            
            if left_depth > right_depth:
                return (left_node, left_depth + 1)
            if right_depth > left_depth:
                return (right_node, right_depth + 1)
            
            # depths equal → this node is LCA of deepest nodes
            return (node, left_depth + 1)
        
        return dfs(root)[0]