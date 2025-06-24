class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        if not heights: return 0
        stack = [] #pair: (index, height)
        max_area = 0
        heights.append(0)  # Sentinel to flush the stack at the end

        for i, h in enumerate(heights):
            start = i
            while stack and h < stack[-1][1]:
                idx, height = stack.pop()
                max_area = max(max_area, height * (i - idx))
                start = idx
            stack.append((start, h))
        
        return max_area