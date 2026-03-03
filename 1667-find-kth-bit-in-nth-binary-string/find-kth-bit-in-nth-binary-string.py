class Solution:
    s = '0'
    def invertReverse(s):
            res = ""
            for i in s:
                if i == "1": 
                    res = "0" + res
                else:
                    res = "1" + res
            return res
        
    for i in range(1,20):
        s = s + "1" + invertReverse(s)

    def findKthBit(self, n: int, k: int) -> str:
        
        return self.s[k-1]