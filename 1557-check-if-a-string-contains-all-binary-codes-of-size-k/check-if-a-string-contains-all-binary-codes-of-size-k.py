class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        setK = set()
        i = 0
        while i + k -1 < len(s):
            setK.add(s[i:i+k])
            i+=1
        return len(setK) == 2**k 