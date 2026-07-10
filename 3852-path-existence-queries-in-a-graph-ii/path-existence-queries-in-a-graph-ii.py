#This was way beyond my level lol
class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[int]:
        nums = [(v, i) for i, v in enumerate(nums)]
        nums.sort()
        ntoi = {}
        for i, (v, node) in enumerate(nums):
            ntoi[node] = i

        maxjumps = [0] * n
        for i, (v, node) in enumerate(nums):
            nxt = bisect.bisect_left(nums, (v + maxDiff, inf)) - 1
            maxjumps[i] = nxt

        LOG = n.bit_length()
        up = [maxjumps]

        for _ in range(1, LOG):
            last = up[-1]
            up.append([last[last[i]] for i in range(n)])
        
        res = []
        for a, b in queries:
            a = ntoi[a]
            b = ntoi[b]
            if a == b: 
                res.append(0)
                continue
            if a > b:
                a, b = b, a
            curr = a
            jumps = 0

            for k in range(LOG - 1, -1, -1):
                if up[k][curr] < b:
                    curr = up[k][curr]
                    jumps += 2**k
            
            if maxjumps[curr] >= b: res.append(jumps + 1)
            else: res.append(-1)
        return res
