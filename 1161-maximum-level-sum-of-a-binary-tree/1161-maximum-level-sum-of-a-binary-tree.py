# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        q = deque([root])
        level = 1
        maxSum = float("-inf")
        answer = level

        while q:
            levelSum = 0

            for _ in range(len(q)):   
                node = q.popleft()
                levelSum += node.val

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            if levelSum > maxSum:
                maxSum = levelSum
                answer = level

            level += 1

        return answer