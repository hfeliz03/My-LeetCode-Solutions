class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        ### Not solved by me
        adj = defaultdict(list)

        for s,e,w in zip(original, changed, cost):
            adj[s].append((w, e))

        @cache
        def dijkstra(s,t):
            d = defaultdict(lambda: inf)
            d[s] = 0
            h = [(0,s)]
            while h: 
                w, node = heapq.heappop(h)
                for nw, nei in adj[node]:
                    if w + nw < d[nei]: 
                        d[nei] = w + nw
                        heapq.heappush(h, (w + nw, nei))
            
            return d[t]

        lengths = sorted(set(len(w) for w in original))

        @cache
        def dp(i):
            if i == len(source): return 0 # base case
            if source[i] == target[i]: best = dp(i+1)
            else: best = inf

            for length in lengths:
                if i + length > len(source): break
                s = source[i:i+length]
                t = target[i:i+length]
                if not s in adj: continue
                best = min(best, dijkstra(s, t) + dp(i + length))
            
            return best
        
        res = dp(0)
        return res if res != inf else -1