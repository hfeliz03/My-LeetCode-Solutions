class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        n = len(nums)
        maxPairs = []
        nums = sorted(nums)
        print(nums)
        # for i, x in enumerate(nums):
        #     curMaxPair = 0
        #     for j, y in enumerate(nums[i+1:]):
        #         curMaxPair = max(curMaxPair, x+y)
        #     maxPairs.append(curMaxPair) if curMaxPair != 0 else maxPairs

        i = 0
        while i < n /2:
            maxPairs.append(nums[i] + nums[n-i-1])
            i+=1

        print(maxPairs)
        return max(maxPairs)