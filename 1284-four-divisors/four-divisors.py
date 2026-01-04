class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        memo = {}  # num -> sum of divisors if exactly 4 divisors, else 0
        total = 0

        for num in nums:
            if num in memo.keys():
                total += memo[num]
                continue

            # Find divisors via sqrt trick
            divs = set([1, num])
            r = int(math.isqrt(num))

            for d in range(2, r + 1):
                if num % d == 0:
                    divs.add(d)
                    divs.add(num // d)
                    if len(divs) > 4:   # early stop, we don't care anymore
                        break

            memo[num] = sum(divs) if len(divs) == 4 else 0
            total += memo[num]

        return total