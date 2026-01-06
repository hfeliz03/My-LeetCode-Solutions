# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        q = deque([(root.left, root.right)])

        while q:
            a, b = q.popleft()

            if a is None and b is None: continue
            if a is None or b is None: return False
            if a.val != b.val: return False

            q.append((a.left, b.right))
            q.append((a.right, b.left))

        return True
            