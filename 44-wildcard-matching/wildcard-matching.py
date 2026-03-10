class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        #? matches one char
        #* matches any number of chars. 0 and 1 included.
        #iterate over the letters in p. if theres a p that is not ? nor *, then theres no way that p will form s
        #if we find a ? simply match its index with the one in s and "skip"
        #if we find * thats when we must start expanding the matching until p[i+1] == s[i] such but it could be the case where this is not enough to update the char and p and proceed to another one, this may be need to be done with DP.
        #If we find a 
        setCharS, setCharP = set(s), set(p)
        unwanted = setCharP.difference(setCharS)
        unwanted.discard("?")
        unwanted.discard("*")
        if len(unwanted) > 0: return False

        n, m = len(p), len(s)
        i = 0
        j = 0
        
        dp = [[False]*(n+1) for _ in range(m+1)]
        dp[0][0] = True

        for j in range(1, n+1): #Asterisc at the beginning
            if p[j-1] == "*":
                dp[0][j] = dp[0][j-1]
        
        for i in range(1, m+1):
            for j in range(1, n+1):
                if p[j-1] == s[i-1] or p[j-1] == "?":
                    dp[i][j] = dp[i-1][j-1]
                elif p[j-1] == "*":
                    dp[i][j] = dp[i][j-1] or dp[i-1][j]

        return dp[m][n]

            