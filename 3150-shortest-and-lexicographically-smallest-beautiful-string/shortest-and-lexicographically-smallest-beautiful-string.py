class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        l = 0
        num1 = 0
        res = ""

        for r in range(len(s)):
            if s[r] == "1":
                num1 += 1

            # Too many 1s -> shrink from left
            while num1 > k:
                if s[l] == "1":
                    num1 -= 1
                l += 1

            # Remove unnecessary leading zeros
            while num1 == k and s[l] == "0":
                l += 1

            if num1 == k:
                cur = s[l:r + 1]

                if (
                    res == ""
                    or len(cur) < len(res)
                    or (len(cur) == len(res) and cur < res)
                ):
                    res = cur

        return res