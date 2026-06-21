class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort(reverse = True)
        i = 0
        while coins >= 0 and i < len(costs):
            curCost = costs[-1-i]
            if coins >= curCost: i += 1
            else: break
            coins -= curCost
        return i
