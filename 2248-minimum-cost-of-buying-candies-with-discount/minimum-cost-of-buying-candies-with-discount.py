class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort()
        res = 0
        while cost:
            res += cost.pop()
            if cost: res += cost.pop()
            if cost: cost.pop()
        return res