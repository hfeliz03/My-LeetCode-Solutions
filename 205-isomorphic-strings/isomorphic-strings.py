class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        sc, tc = defaultdict(list), defaultdict(list) 
        for i in range(len(s)):
            if len(sc) != len(tc): return False
            sc[s[i]].append(i)
            tc[t[i]].append(i)

        return list(tc.values()) == list(sc.values())
