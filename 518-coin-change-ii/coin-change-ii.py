from collections import deque
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # @cache
        # def dfs(startIndex, curSum):
        #     if curSum == amount:
        #         return 1
        #     if curSum > amount:
        #         return 0
        #     res = 0
        #     for j in range(startIndex, len(coins)):
        #         res += dfs(j, curSum + coins[j])
        #     return res
        # return dfs(0, 0)


        # if amount == 0: return 1
        # res = 0 
        # # #     1 2 5 
        # # 0   1 2 3 X
        # # 0.  2   4 X
        # # 0.  5.    X
        # # 1   2 3 4 X
        # # 2.  3   5 X
        # # 2.  4   X X
        # # 1.  3 4 5 X
        # # 2.  4   X X
        # # 1.  4 5 X X

        # #[startCol, curSum, coli, colj,....colk]
        # dp = deque([])
        # for i, val in enumerate(coins):
        #     if val == amount: 
        #         res += 1
        #     elif val < amount:
        #         dp.append([i, val])


        # n = len(coins)
        # i = 1
        # while dp:
        #     curRow = dp.popleft()
        #     for j in range(curRow[0],n):
        #         newSum = curRow[1] + coins[j]
        #         if newSum == amount:
        #             res += 1
        #             continue
        #         elif newSum > amount: continue
        #         dp.append([j, newSum])

        # return res
        #This was really hard, answer not mine
        dp = [0] * (amount + 1)
        dp[0] = 1

        for coin in coins:
            for curAmount in range(coin, amount + 1):
                dp[curAmount] += dp[curAmount - coin]

        return dp[amount]