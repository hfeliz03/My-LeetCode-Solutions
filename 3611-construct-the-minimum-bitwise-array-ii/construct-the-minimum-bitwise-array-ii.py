class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        ans = []
        for num in nums:
            if num % 2 == 0: 
                ans.append(-1)
                continue

            numBi = bin(num)[2:]
        
            for i in range(len(numBi)):
                if numBi[i] == "0": 
                    continue

                curBinaryStr = list(numBi)
                curBinaryStr[i] = "0" 
                curBinaryStr = "".join(curBinaryStr)
                curBinaryInt = int(curBinaryStr, 2)

                if (curBinaryInt|(curBinaryInt + 1)) == num:
                    ans.append(curBinaryInt)
                    break
        
        return ans