class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [-1]*n 
        for x, num in enumerate(nums):
            if num % 2 == 0: continue
            numBi = bin(num)[2:]
        
            for i in range(len(numBi)):
                if numBi[i] == "0": continue
                curBinaryStr = list(numBi)
                curBinaryStr[i] = "0" 
                curBinaryStr = "".join(curBinaryStr)
                curBinaryInt = int(curBinaryStr, 2)
                print(curBinaryInt)
                print(curBinaryInt + 1)
                print(curBinaryInt | (curBinaryInt + 1))
                print("HHH")
                if (curBinaryInt|(curBinaryInt + 1)) == num:
                    
                    ans[x] = curBinaryInt
                    break
        
        return ans