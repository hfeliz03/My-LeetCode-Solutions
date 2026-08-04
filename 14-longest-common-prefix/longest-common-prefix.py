class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        longestCommonPrefix = ""
        if len(strs) == 1: return strs[0]
        minLen = min([len(s) for s in strs])
        for i in range(minLen):
            if set([s[i] for s in strs[1:]]) != set(strs[0][i]):
                break
            else: 
                longestCommonPrefix += strs[0][i]
        return longestCommonPrefix