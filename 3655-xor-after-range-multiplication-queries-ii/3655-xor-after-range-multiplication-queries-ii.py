class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        #This was insane, but it taught me "prefix"-product arrays
        MOD = 10**9 + 7
        n = len(nums)
        sq = int(sqrt(n))
        mp = defaultdict(list)
        
        for l, r, k, v in queries:
            if k > sq:
                for i in range(l, r+1, k):
                    nums[i] = (nums[i] * v) % MOD
            else: 
                mp[k].append((l,r,v))

        for k in mp:
            diff = [1] * (n+k)
            for l, r, v in mp[k]:
                diff[l] = (diff[l] * v) % MOD
                rplus1 = l + ((r-l) // k+1) * k #l + items * size of each step
                diff[rplus1] = (diff[rplus1] * pow(v, -1, MOD)) % MOD
            
            for i in range(k, n):
                diff[i] = (diff[i] * diff[i-k]) % MOD
            
            for i in range(n):
                nums[i] = (diff[i] * nums[i]) % MOD
        
        res = 0
        for x in nums: res ^= x
        return res