class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # We can have a 2D array representing row one string, col the other. 
        #   a c e
        # a 3
        # b.2 2 1  
        # c 2 2 1 0
        # d 1 1 1 0
        # e 1 1 1 0
        # 0 0 0 0 0
        # At DP[n,m] we have that they are common because "" and "" is common
        # then we start checking if s1[i] == s2[j-1], then the curr subsequence updates by 1
        # after we fill up the table we trace which path led to the longest subsequence, by checking the lenght of the string we created
        n = len(text1)
        m = len(text2)
        dp = [[0]*(m+1) for _ in range(n+1)]
        for i in range(n-1,-1,-1):
            for j in range(m-1,-1,-1):
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i+1][j+1]
                dp[i][j] = max(dp[i][j], dp[i+1][j], dp[i][j+1])
                
        return(dp[0][0])