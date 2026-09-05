class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        maxLeft = [nums[0]]
        minRight = [nums[-1]]
        for num in nums[1:]:
            maxLeft.append(max(num, maxLeft[-1]))
        
        for num in nums[len(nums)-2::-1]:
            minRight.append(min(num, minRight[-1]))
        
        minRight = minRight[::-1]
        res = -1
        for i in range(len(nums)):
            if maxLeft[i] - minRight[i] <= k:
                res = i
                break
        
        return res