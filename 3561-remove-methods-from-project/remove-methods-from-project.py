class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        #1 -> 2
        #0 -> 2
        #0 -> 1
        #3 -> 4
        #all sus nodes 0, 1, 2
        #0,2 doesnt point to anything, stop iterating
        #0,1,2 all sus
        #Does anything go into 0,1,2? no? then remove them
        sus = {k}
        # for a,b in invocations:
        #     if a == k:
        #         sus.add(b)
        print(sus)
        adj = defaultdict(list)
        for a,b in invocations:
            adj[a].append(b)
        print(adj)

        #Now do DFS on the elements in sus
        def dfs(node):
            nonlocal sus
            for invoked in adj[node]:
                if invoked not in sus:
                    sus.add(invoked)
                    dfs(invoked)

        dfs(list(sus)[0])
        print(f"{sus=}")
        for a,b in invocations:
            if a not in sus and b in sus:
                print(f"{a=}, {b=}")
                return list(set(range(n)))

        return list(set(range(n)) - sus) 