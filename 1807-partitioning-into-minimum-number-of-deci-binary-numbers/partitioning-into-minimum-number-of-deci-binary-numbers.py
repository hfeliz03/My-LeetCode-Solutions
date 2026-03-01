class Solution:
    def minPartitions(self, n: str) -> int:
        res = 0
        for c in n:
            res = max(res, int(c))
        return res

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