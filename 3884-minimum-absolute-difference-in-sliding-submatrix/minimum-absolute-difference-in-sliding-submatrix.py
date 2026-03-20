class Solution:
    def minAbsDiff(self, grid: List[List[int]], k: int) -> List[List[int]]:
        if not grid: return 0
        m, n = len(grid), len(grid[0])
        ans = [[0]*(n-k+1) for _ in range(m-k+1)]
        for i in range(m):
            for j in range(n):
                if i + k <= m and j + k <=n:
                    currSet = set()
                    for ii in range(i, i + k):
                        for jj in range(j, j + k):
                            currSet.add(grid[ii][jj])
                    if len(currSet) == 1: ans[i][j]=0
                    else:
                        sortedList = sorted(list(currSet))
                        num = 1
                        curMin = 10**10                        
                        while num < len(sortedList):
                            curMin = min(abs(sortedList[num] - sortedList[num-1]), curMin)
                            num+=1
                        ans[i][j] = curMin
        return ans