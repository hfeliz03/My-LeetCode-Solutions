class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        pos = [nums[0]]
        neg = [-nums[0]]
        for num in nums[1:]:
            #print(pos, neg)
            temp = pos.copy()
            pos = [x+num for x in pos] + [x+num for x in neg]
            neg = [x-num for x in temp] + [x-num for x in neg]
        res = len([num for num in pos if num == target] + [num for num in neg if num == target])
        return res