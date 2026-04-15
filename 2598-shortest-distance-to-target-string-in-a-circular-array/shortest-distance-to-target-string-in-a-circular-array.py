class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        if target not in set(words): return -1
        res = 10**5
        n = len(words)
        for i in range(n):
            if words[(startIndex + i ) % n] == target: 
                res = i
                break
            elif words[(startIndex - i + n ) %n] == target:
                res = i
                break
        return res