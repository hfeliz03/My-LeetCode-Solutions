class Solution:
    def minimumCost(self, nums: List[int], k: int, dist: int) -> int:
        n = len(nums)
        small, large = SortedList(), SortedList()
        
        #initial window
        for i in range(1, dist + 2): #non inclusive, up to dist + 1
            small.add((nums[i], i))
        while len(small) >= k: large.add(small.pop(-1)) #redistribute to large if small overflown
        curr = sum(v for v, _ in small)
        res = curr

        for i in range(dist+2, n):
            pkey = (nums[i - dist - 1], i - dist - 1)
            nkey = (nums[i], i)

            #remove left
            if pkey in small:
                small.discard(pkey)
                curr -= nums[i - dist -1]
                if large: 
                    l = large.pop(0)
                    small.add(l)
                    curr += l[0]
            elif pkey in large:
                large.discard(pkey)

            #add right
            small.add(nkey)
            curr += nums[i]

            if len(small) >= k:
                s = small.pop(-1)
                large.add(s)
                curr -= s[0]

            res = min(res, curr)
        return res+ nums[0]