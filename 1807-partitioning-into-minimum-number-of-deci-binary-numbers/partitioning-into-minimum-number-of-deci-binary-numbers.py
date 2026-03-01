class Solution:
    def minPartitions(self, n: str) -> int:
        nAsArr = [int(c) for c in n]
        return max(nAsArr)
        
        # count = 0
        # s = ""
        # for i in range(len(n)):s += "1"
        # n = int(n)
        # while n > 0:
            
        #     sInt = int(s)
        #     if sInt <= n:
        #         n -= sInt
        #         count += 1
        #     else:
        #         s = bin(int(s,2)-1)[2:]


        # return count