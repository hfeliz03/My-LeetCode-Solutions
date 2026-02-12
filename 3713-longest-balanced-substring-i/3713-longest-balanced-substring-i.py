class Solution:
    def longestBalanced(self, s: str) -> int:
        n = len(s)
        curLongestSubstring = 0
        for i in range(n):
            setChars = {}        
            for j in range(i, n):
                setChars[s[j]] = setChars.get(s[j], 0) + 1
                lastAdded = setChars[s[j]]
                if all(element == lastAdded for element in setChars.values()):
                    curLongestSubstring = max(curLongestSubstring, j-i+1)
        return curLongestSubstring
