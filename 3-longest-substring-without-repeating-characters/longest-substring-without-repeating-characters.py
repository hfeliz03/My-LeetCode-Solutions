class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s: return 0
        seen, longest, j = set(), 0, 0
        for i in range(len(s)):
            while s[i] in seen:
                seen.remove(s[j])
                j += 1
            seen.add(s[i])
            longest = max(longest, i - j + 1)
        
        return longest