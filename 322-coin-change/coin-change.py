class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        DP = [10**5] * (amount+1)
        DP[0] = 0
        coins.sort(reverse = True)
        i = 1
        while i < len(DP):
            for coin in coins:
                if coin > i: continue
                else:       #9-7 j = 9-7=2
                    if i - coin == 0: 
                        DP[i] = 1
                        break
                    else:               #i+1 - coin > 0
                        j = i - coin
                        DP[i] = min(DP[i], 1+DP[j])
            i+=1
                    
        print(DP)
        return DP[-1] if DP[-1] != 10**5 else -1