class Solution:
    def minElement(self, nums: List[int]) -> int:
        minNum = 10**5
        for num in nums:
            numArr = list(str(num))
            sumNumArr = 0
            print(numArr)
            for numStr in numArr: 
                numStr = int(numStr)
                sumNumArr += numStr
            minNum = min(minNum, sumNumArr)
        return minNum