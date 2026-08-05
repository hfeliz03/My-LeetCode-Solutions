class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged = []
        isWord1Longer = True if len(word1) >= len(word2) else False
        n = len(word2) if isWord1Longer else len(word1)

        for i in range(n):
            merged += [word1[i]] + [word2[i]]

        merged += word1[n:] if isWord1Longer else word2[n:]
        return "".join(merged)