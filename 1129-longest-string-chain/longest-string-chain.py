import re 
class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        res = 1
        words.sort(key = len)
        print(words)
        dp = {}

        for word in words:
            dp[word] = 1
            for i in range(len(word)):
                rmvOne = word[:i] + word[i+1:]
                print(rmvOne)
                if rmvOne in dp:
                    dp[word] = max(dp[word], dp[rmvOne]+1)
            res = max(res, dp[word])

        return res
