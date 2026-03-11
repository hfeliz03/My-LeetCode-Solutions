class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle)>len(haystack): return -1
        if len(needle)==len(haystack): return -1 if needle!=haystack else 0
        j = len(needle)
        i = 0
        while j <= len(haystack):
            if haystack[i:j] == needle: return i
            i+=1
            j+=1
        return -1