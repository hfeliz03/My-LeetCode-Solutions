from typing import List

class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0

        cols = len(matrix[0])
        heights = [0] * cols
        best = 0

        for row in matrix:
            # Build histogram heights for this row
            for j in range(cols):
                if row[j] == "1":
                    heights[j] += 1
                else:
                    heights[j] = 0

            best = max(best, self.largestRectangleArea(heights))

        return best

    def largestRectangleArea(self, heights: List[int]) -> int:
        # Monotonic increasing stack of indices
        stack = []
        max_area = 0

        # Add a sentinel 0 height to flush the stack at the end
        extended = heights + [0]

        for i, h in enumerate(extended):
            while stack and extended[stack[-1]] > h:
                height = extended[stack.pop()]
                left_smaller_index = stack[-1] if stack else -1
                width = i - left_smaller_index - 1
                max_area = max(max_area, height * width)
            stack.append(i)

        return max_area