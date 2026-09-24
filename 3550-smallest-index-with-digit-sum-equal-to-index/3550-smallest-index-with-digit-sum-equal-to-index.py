class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i, num in enumerate(nums):
            numStr = str(num)
            sumDigits = 0
            for digit in numStr: 
                sumDigits += int(digit)
            if sumDigits == i: return i
        return -1