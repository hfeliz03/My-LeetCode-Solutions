class Solution:
    def minCost(self, n: int, edges: List[List[int]]) -> int:
        # revEdges = []
        # for edge in edges:
        #     revEdges.append([edge[1], edge[0], 2*edge[2]])
        
        # undirected = sorted(edges + revEdges)
        # starters = [starter for starter in undirected if starter[0] == 0]

        # def bfs(edge, curCost, curEdges):
        #     if edge[1] == n-1: return edge[2] + curCost
        #     else:
        #         nextEdges = [nextEdge for nextEdge in curEdges if nextEdge[0] == edge[1] and nextEdge[1] != edge[0]]
        #         return min([bfs(nextEdge, edge[2] + curCost, curEdges - nextEdges) for nextEdge in nextEdges])

        # return min([bfs(starter, 0, undirected - starters) for starter in starters])
        # print(undirected)
        # print(starters)
        # Build adjacency list with both directions:
        # u -> v costs w
        # v -> u costs 2w
        adj = [[] for _ in range(n)]
        for u, v, w in edges:
            adj[u].append((v, w))
            adj[v].append((u, 2 * w))

        INF = 10**18
        dist = [INF] * n
        dist[0] = 0

        pq = [(0, 0)]  # (cost, node)
        while pq:
            cost, u = heapq.heappop(pq)
            if cost != dist[u]:
                continue
            if u == n - 1:
                return cost

            for v, w in adj[u]:
                nc = cost + w
                if nc < dist[v]:
                    dist[v] = nc
                    heapq.heappush(pq, (nc, v))

        return -1  # if unreachable