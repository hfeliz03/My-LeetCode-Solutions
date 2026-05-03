from collections import Counter 
class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal) or Counter(s) != Counter(goal): return False
        n = len(s)
        s += s
        for i in range(n):
            if s[i:i+n] == goal : return True

        return False