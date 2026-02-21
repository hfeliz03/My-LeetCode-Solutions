class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)
        memo = {}

        def helper(s):
            if not s: return True
            if s in memo: return memo[s]

            memo[s] = False
            for j in range(1,len(s)+1):
                if s[:j] in wordSet and helper(s[j:]):
                    memo[s] = True
                    break
            
            return memo[s]
        
        return helper(s)