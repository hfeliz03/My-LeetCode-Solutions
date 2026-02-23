class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        setK = set()
        for i in range(2**k):
            setK.add(bin(i)[2:].zfill(k))
        i = 0
        while i + k -1 < len(s):
            if s[i:i+k] in setK:
                setK.remove(s[i:i+k])
            i+=1
        return len(setK) == 0 