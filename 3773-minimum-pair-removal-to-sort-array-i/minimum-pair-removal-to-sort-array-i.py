class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:

        def helper(nums, numOps):
            if len(nums) <= 1 or all(nums[i] <= nums[i+1] for i in range(len(nums)-1)):
                return numOps

            # find adjacent pair with minimum sum
            indToMerge = 0
            curMin = float("inf")
            for i in range(len(nums) - 1):
                pair_sum = nums[i] + nums[i+1]
                if pair_sum < curMin:
                    curMin = pair_sum
                    indToMerge = i

            # merge nums[indToMerge] and nums[indToMerge+1]
            numsMerged = (
                nums[:indToMerge]
                + [nums[indToMerge] + nums[indToMerge + 1]]
                + nums[indToMerge + 2:]
            )

            return helper(numsMerged, numOps + 1)

        return helper(nums, 0)

