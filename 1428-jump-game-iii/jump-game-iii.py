class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        n = len(arr)
        alrVisited = set()
        
        def dfs(i):    
            if i < 0 or i >= n or i in alrVisited: return False 
            if arr[i] == 0: return True
            alrVisited.add(i)
            return dfs(i + arr[i]) or dfs(i - arr[i])


        return dfs(start + arr[start]) or dfs(start - arr[start])