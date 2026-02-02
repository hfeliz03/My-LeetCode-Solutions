class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        minCost = [nums[0], 10**5, 10**5]
        for i in nums[1:]:
            if i < minCost[1]:
                minCost[2] = minCost[1]
                minCost[1] = i
            elif i < minCost[2]:
                minCost[2] = i
        return sum(minCost)