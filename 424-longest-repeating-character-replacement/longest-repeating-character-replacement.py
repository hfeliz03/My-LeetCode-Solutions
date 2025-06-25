class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count, longestCharRep = {}, 0

        l= maxf = 0

        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0) #Increment the frequency of such char
            maxf = max(maxf, count[s[r]])

            if (r-l+1) - maxf > k: #Not enough k's to replace the different letters 
                count[s[l]] -= 1
                l += 1
            
            longestCharRep = max(longestCharRep, r-l+1)
        
        return longestCharRep