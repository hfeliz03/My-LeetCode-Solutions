class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        if target not in set(words): return -1
        minDis = 10**5
        disForward = disBackward = 10**5
        n = len(words)
        for i in range(n):
            if words[(startIndex + i ) % n] == target: 
                disForward = i
                break
        for i in range(n):
            if words[(startIndex - i + n ) %n] == target:
                disBackward = i
                break
        return min(disForward, disBackward)