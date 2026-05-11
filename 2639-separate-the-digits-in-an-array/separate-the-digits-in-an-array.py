class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        return [int(char) for num in nums for char in str(num)]