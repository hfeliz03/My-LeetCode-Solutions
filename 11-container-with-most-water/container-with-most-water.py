class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        l, r = 0, n-1
        maxWater = 0
        while l < r:
            h = min(height[l], height[r])
            w = r - l
            maxWater = max(maxWater, h*w)
            if h == height[l]: l += 1
            else: r-= 1
        return maxWater
