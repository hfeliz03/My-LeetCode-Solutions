class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        n, maxPairs, i = len(nums), [], 0
        nums.sort()
        while i < n /2:
            maxPairs.append(nums[i] + nums[n-i-1])
            i+=1

        return max(maxPairs)