class Solution:
    def minOperations(self, s: str) -> int:
        if len(s) <= 1: return 0
        start1 = "1"
        start0 = "0"
        for i in range(len(s)-1):
            start1, start0 = start1 + start0[-1], start0 + start1[-1]

        print(start1)
        print(start0)
        count0 = count1 = 0
        for i, char in enumerate(s):
            if char != start1[i]:
                count1 += 1
            if char != start0[i]:
                count0 += 1 
                
        return min(count1, count0)