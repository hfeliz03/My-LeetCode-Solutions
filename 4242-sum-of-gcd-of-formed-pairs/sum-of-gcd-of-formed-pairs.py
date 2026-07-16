class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        prefixGcd = []
        curMax = -10**5
        for num in nums:   
            curMax = max(curMax, num)
            prefixGcd.append(gcd(curMax, num))
        prefixGcd.sort()
        pairs = []
        i, j = 0, len(prefixGcd)-1
        while i < j :
            pairs.append(gcd(prefixGcd[i], prefixGcd[j]))
            i += 1
            j -= 1
        return sum(pairs)