class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
        q = len(queries)
        res = [-1] * q
        farthestI = [-1] * n
        for i in range(n-1,-1,-1):
            if i == n-1: continue
            farthestI[i] = i if abs(nums[i+1]-nums[i]) > maxDiff else farthestI[i+1]

        for i in range(q):
            res[i] = False if farthestI[queries[i][0]] != farthestI[queries[i][1]] else True

        return res