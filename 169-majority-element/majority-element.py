from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        half = len(nums)//2
        freqs = Counter(nums)
        maxAppearances = max(freqs.values())
        majorityElement = 0
        for key, val in freqs.items():
            if val == maxAppearances: 
                majorityElement = key
                break

        return majorityElement