class UF: 
    #I DID NOT SOLVE THIS PROBLEM
    def __init__(self, n):
        self.par = [i for i in range(n)]
        self.rank = [0]*n
    
    def find(self, x):
        if self.par[x] != x:
            self.par[x] = self.find(self.par[x])
        return self.par[x]

    def union(self, x, y):
        px = self.find(x)
        py = self.find(y)

        if self.rank[px] < self.rank[py]:
            self.par[px] = py
        elif self.rank[py] < self.rank[px]:
            self.par[py] = px
        else: 
            self.rank[px] += 1
            self.par[py] = px

        
class Solution:
    def maxStability(self, n: int, edges: List[List[int]], k: int) -> int:
        uf = UF(n)
        used = 0
        opt = []
        res = inf

        for x, y, s, m in edges:
            if m: 
                if uf.find(x) == uf.find(y): return -1
                uf.union(x,y)
                used+=1
                res = min(res, s)
            else: 
                opt.append((x,y,s,m))
            
        opt.sort(key = lambda x: x[2], reverse = True)
        simple = inf
        upgraded = inf
        for i in range(len(opt)):
            x, y, s, m = opt[i]
            if uf.find(x) == uf.find(y) : continue
            uf.union(x, y)
            used += 1
            if used == n - 1 - k: simple = s
            upgraded = s
        
        if used != n-1: return -1
        return min(res, simple, upgraded*2)