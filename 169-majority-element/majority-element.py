from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        freqs = Counter(nums)
        maxAppearances = max(freqs.values())
        for key, val in freqs.items():
            if val == maxAppearances: 
                return key

        return -1