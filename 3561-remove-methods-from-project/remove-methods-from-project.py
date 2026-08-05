class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        sus = {k}
        adj = defaultdict(list)
        for a,b in invocations:
            adj[a].append(b)

        #Now do DFS on the elements in sus
        def dfs(node):
            nonlocal sus
            for invoked in adj[node]:
                if invoked not in sus:
                    sus.add(invoked)
                    dfs(invoked)

        dfs(list(sus)[0])

        for a,b in invocations:
            if a not in sus and b in sus:
                return list(set(range(n)))

        return list(set(range(n)) - sus) 