class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        numsSet = set(nums)
        seqSum = nums[0]

        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] + 1:
                seqSum += nums[i]
            else:
                break

        while seqSum in numsSet:
            seqSum += 1

        return seqSum