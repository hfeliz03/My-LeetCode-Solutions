#Did not solve this one. I was able to get to a better than bruteforce solution, but 
#Learned that there is a maxium of 4300 digits for string to int conversion lol
class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        MOD = 10**9 + 7
        solendivar = (s, queries)

        n = len(s)

        prefix_sum = [0] * (n + 1)
        prefix_count = [0] * (n + 1)
        prefix_num = [0] * (n + 1)
        pow10 = [1] * (n + 1)

        for i in range(n):
            pow10[i + 1] = (pow10[i] * 10) % MOD

        for i, ch in enumerate(s):
            d = int(ch)

            prefix_sum[i + 1] = prefix_sum[i] + d
            prefix_count[i + 1] = prefix_count[i]
            prefix_num[i + 1] = prefix_num[i]

            if d != 0:
                prefix_count[i + 1] += 1
                prefix_num[i + 1] = (prefix_num[i] * 10 + d) % MOD

        res = []

        for l, r in queries:
            digit_sum = prefix_sum[r + 1] - prefix_sum[l]
            k = prefix_count[r + 1] - prefix_count[l]
            x = (prefix_num[r + 1] - prefix_num[l] * pow10[k]) % MOD
            res.append((x * digit_sum) % MOD)

        return res