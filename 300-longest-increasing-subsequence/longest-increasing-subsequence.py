class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        subSeq = [1] * len(nums)

        for i in range(len(subSeq)-2, -1, -1):
            for j in range(i+1, len(subSeq)):
                if nums[j] > nums[i]:
                    subSeq[i] = max(subSeq[j] + 1, subSeq[i])
        print(subSeq)
    
        return max(subSeq)