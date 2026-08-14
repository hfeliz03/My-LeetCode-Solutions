class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        l = 0
        res = 0
        ctr = defaultdict(int)
        for r, char in enumerate(s):
            ctr[char] += 1
            step = 0
            while ctr[char] > 2:
                ctr[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)

        return res