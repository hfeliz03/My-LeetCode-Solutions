from collections import Counter
class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        n = len(s1)
        s1evens, s1odds, s2evens, s2odds = [], [], [], []
        for i in range(n):
            if i % 2 == 0:
                s1evens.append(s1[i])
                s2evens.append(s2[i])
            else:
                s1odds.append(s1[i])
                s2odds.append(s2[i])
        s1evens = Counter(s1evens)
        s1odds = Counter(s1odds)
        s2evens = Counter(s2evens)
        s2odds = Counter(s2odds)

        return s1evens == s2evens and s1odds == s2odds