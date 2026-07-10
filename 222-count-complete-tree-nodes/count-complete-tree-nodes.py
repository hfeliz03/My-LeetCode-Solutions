# # Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, val=0, left=None, right=None):
# #         self.val = val
# #         self.left = left
# #         self.right = right
# class Solution:
#     def countNodes(self, root: Optional[TreeNode]) -> int:
#         count = 0
#         def helper(curr):
#             nonlocal count
#             if not curr: return 
#             count += 1
#             helper(curr.left)
#             helper(curr.right)
#         helper(root)
#         return count

# class Solution:
#     def countNodes(self, root: Optional[TreeNode]) -> int:
#         if not root:
#             return 0

#         return 1 + self.countNodes(root.left) + self.countNodes(root.right)
#How on earth can this be easy lmao
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        left_height = self.get_height(root.left)
        right_height = self.get_height(root.right)

        if left_height == right_height:
            return (2 ** left_height) + self.countNodes(root.right)

        return (2 ** right_height) + self.countNodes(root.left)

    def get_height(self, node: Optional[TreeNode]) -> int:
        height = 0

        while node:
            height += 1
            node = node.left

        return height