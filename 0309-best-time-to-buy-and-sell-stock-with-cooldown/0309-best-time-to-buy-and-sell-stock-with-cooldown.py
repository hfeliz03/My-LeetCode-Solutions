# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         if not prices: return 0

#         n = len(prices)
#         res = 0
#         seen = {}

#         def helper(i: int, prev: str, curr: int, stock: bool):
#             nonlocal res

#             state = (i, prev, stock)
#             if seen.get(state, float("-inf")) >= curr:
#                 return
#             seen[state] = curr

#             res = max(res, curr)

#             i += 1
#             if i == n: return

#             if prev == "c":
#                 if not stock:
#                     helper(i, "b", curr - prices[i], True)
#                 else:
#                     helper(i, "s", curr + prices[i], False)

#             elif prev == "b":
#                 helper(i, "s", curr + prices[i], False)

#             helper(i, "c", curr, stock)

#         helper(-1, "b", -prices[0], True)
#         helper(-1, "c", 0, False)

#         return res

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        @cache
        def helper(i: int, stock: bool, cooldown: bool) -> int:
            if i == n:
                return 0

            # Skip today
            res = helper(i + 1, stock, False)

            if stock:
                # Sell today, causing cooldown tomorrow
                res = max(
                    res,
                    prices[i] + helper(i + 1, False, True)
                )

            elif not cooldown:
                # Buy today
                res = max(
                    res,
                    -prices[i] + helper(i + 1, True, False)
                )

            return res

        return helper(0, False, False)