class Solution:
    def longestBalanced(self, s: str) -> int:
        single = ("z", -1)
        maxSingle = 0
        for i in s:
            if i != single[0]: 
                single = (i, 1)
            else:
                single = (single[0], single[1]+1)
            maxSingle = max(maxSingle, single[1])

        maxDouble = 0
        pairs = [("a","b"), ("a","c"), ("b","c")]

        for x, y in pairs:
            cx = cy = 0
            first = {0: -1}   # diff -> earliest index (within current valid segment)
            for i, ch in enumerate(s):
                if ch != x and ch != y:
                    cx = cy = 0
                    first = {0: i}   # reset segment start at i
                    continue

                if ch == x: cx += 1
                else: cy += 1

                diff = cx - cy
                if diff not in first:
                    first[diff] = i
                else:
                    maxDouble = max(maxDouble, i - first[diff])

        maxTripl = 0
        hashPair = {(0,0):-1}
        letter = {"a" : 0, "b" : 0, "c" : 0}
        for i in range(len(s)):
            letter[s[i]] += 1
            curHashPair = (letter["b"] - letter["a"], letter["c"] - letter["a"])
            if curHashPair not in hashPair.keys():
                hashPair[curHashPair] = i
            else:
                maxTripl = max(maxTripl, i - hashPair[curHashPair])

        return max(maxSingle, maxDouble, maxTripl)