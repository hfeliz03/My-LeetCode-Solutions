class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        freq = {}
        for i in nums:
            if i in freq.keys():
                return True
            else: freq[i] = 1
        return False