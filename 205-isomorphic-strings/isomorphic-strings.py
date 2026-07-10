class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        # sc = Counter(s)
        # tc = Counter(t)
        # if sc == tc: return True
        # for keys in list(sc):
        #     if keys in tc:
        #         del sc[keys]
        #         del tc[keys]
        # return sorted(list(sc.values())) == sorted((list(tc.values())))
        sc, tc = defaultdict(list), defaultdict(list) 
        for i in range(len(s)):
            if len(sc) != len(tc): return False

            sc[s[i]].append(i)
            tc[t[i]].append(i)
        print(sc)
        print(tc)
        print(sc.values())
        print(tc.values)
        return list(tc.values()) == list(sc.values())
