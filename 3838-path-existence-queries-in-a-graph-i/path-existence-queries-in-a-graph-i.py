class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
        q = len(queries)
        res = [-1] * q
        #check in reverse all the connections
        #for each num create an array that stores how far (the index) it can get
        #example 2: 
        #0,n,n,n
        farthestI = [i for i in range(n)]
        for i in range(n-1,-1,-1):
            if i == n-1: continue
            farthestI[i] = i if abs(nums[i+1]-nums[i]) > maxDiff else farthestI[i+1]
        for i in range(len(res)):
            res[i] = False if farthestI[queries[i][0]] != farthestI[queries[i][1]] else True
        print(farthestI)
        return res