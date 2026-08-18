class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        n = len(nums)

        if k == n: 
            return max(nums)

        ctr = Counter(nums)
        res = -1
        if k == 1: 
            for num in nums:
                if ctr[num] == 1: res = max(res, num)
            return res
        else:
            first, last = nums[0] if ctr[nums[0]] == 1 else -1 , nums[-1] if ctr[nums[-1]] == 1 else -1
            return max(first, last)


