class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        # let n = 3
        # nums = 6
        # unique = 3+1 = 4
        # therefore 1 element appears 3 times
        setNums = set()
        for i in nums:  
            if i not in setNums: setNums.add(i)
            else: return i
        return