class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        if not s: return 0
        longest = 0 
        j = 0
        for i in range(len(s)):
            while s[i] in seen:
                seen.remove(s[j])
                j += 1
            seen.add(s[i])

            longest = max(longest, i - j + 1)
        
        return longest