class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        # l, r = 0 , len(nums) - 1
        # cnt = 0
        # while l <= r and x > 0:
        #     if nums[l] < nums[r] and nums[l] <= x:
        #         x -= nums[l]
        #         l += 1
        #     elif nums[l] >= nums[r] and nums[r] <= x:
        #         x -= nums[r]
        #         r -= 1
        #     elif max(nums[l], nums[r]) <= x:
        #         x -= max(nums[l], nums[r])
        #         if nums[l] < nums[r]: l += 1
        #         else: r -= 1
        #     else: break
        #     cnt += 1

        # return cnt if x == 0 else -1
        # cnt = 0
        # maxSubarr = 0
        # for num in nums:
        #     if num <= x:
        #         x -= num
        #         cnt += 1
        # return cnt if x == 0 else -1


        target = sum(nums) - x

        if target < 0: return -1

        l = 0
        curSum = 0
        maxLen = -1

        for r in range(len(nums)):
            curSum += nums[r]
            while curSum > target and l <= r:
                curSum -= nums[l]
                l += 1
            if curSum == target:
                maxLen = max(maxLen, r - l + 1)

        return len(nums) - maxLen if maxLen != -1 else -1