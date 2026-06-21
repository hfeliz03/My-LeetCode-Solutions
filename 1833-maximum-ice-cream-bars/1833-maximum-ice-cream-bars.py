class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort(reverse = True)
        res = 0
        while coins >= 0 and costs:
            curCost = costs.pop()
            if coins>= curCost: res += 1
            coins -= curCost
        return res
