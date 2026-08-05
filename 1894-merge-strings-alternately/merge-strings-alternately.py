class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged = ""
        longer = word1 if len(word1) >= len(word2) else word2
        shorter = word1 if len(word1) < len(word2) else word2

        for i in range(len(shorter)):
            merged += word1[i] + word2[i]

        merged += longer[len(shorter):]
        return merged