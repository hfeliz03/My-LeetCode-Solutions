class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        #This is insane, i didnt even get it
        @cache
        def sum_same_len(limit):
            s = str(limit)
            arr = []
            for c in s: arr.append(int(c))

            n = len(arr)
            
            @cache
            def dp(i, prev, tight, curr, trend):
                if i == n: return curr
                mx = arr[i] if tight else 9
                res = 0

                for d in range(mx + 1):
                    if i == 0 and d == 0: continue

                    ntight = tight and d == mx

                    ncurr = curr
                    if trend == 1 and d < prev: ncurr += 1
                    elif trend == 2 and d > prev: ncurr += 1

                    if d == prev or i == 0: ntrend = 0
                    elif d > prev: ntrend = 1
                    elif d < prev: ntrend = 2
                    
                    res += dp(i+1, d, ntight, ncurr, ntrend)

                return res
            return dp(0, 0, True, 0, 0)
        
        @cache
        def sum_up_to(limit):
            totald = len(str(limit))
            res = 0

            for digits in range(1, totald):
                largest = 10**digits - 1 #9, 99, 999, etc
                res += sum_same_len(largest)
            
            res += sum_same_len(limit) 
            return res
        
        res = sum_up_to(num2) - sum_up_to(num1)

        s = str(num1)
        for i in range(1, len(s) - 1):
            if s[i - 1] < s[i] > s[i+1] or s[i-1] > s[i] < s[i+1]:
                res += 1
        return res
