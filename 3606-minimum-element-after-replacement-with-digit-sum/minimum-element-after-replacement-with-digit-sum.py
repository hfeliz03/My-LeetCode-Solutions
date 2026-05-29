class Solution:
    def minElement(self, nums: List[int]) -> int:
        minNum = 10**5
        for num in nums:
            numArr = str(num)
            sumNumArr = 0
            for numStr in numArr: 
                sumNumArr += int(numStr)
            minNum = min(minNum, sumNumArr)
        return minNum