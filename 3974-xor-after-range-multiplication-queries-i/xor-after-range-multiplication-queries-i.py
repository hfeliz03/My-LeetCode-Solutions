class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        if not nums or not queries: return nums
        for li, ri, ki, vi in queries:
            idx = li
            
            while idx <= ri:
                nums[idx] = (nums[idx] * vi) % (10**9 + 7)
                idx += ki
        res = 0
        for elem in nums: res = res ^ elem
        return res
