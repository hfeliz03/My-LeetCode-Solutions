class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        charsToChange = []
        totalCost = 0

        if source == target : return totalCost
        
        INF = 10**18
        # 26 letters
        dist = [[INF] * 26 for _ in range(26)]
        for i in range(26):
            dist[i][i] = 0

        # direct edges (take min if multiple edges for same pair)
        for o, c, w in zip(original, changed, cost):
            u = ord(o) - ord('a')
            v = ord(c) - ord('a')
            if w < dist[u][v]:
                dist[u][v] = w #As of now, dist[u][v] can only be infinity or direct transition
        
        # Floyd-Warshall
        for k in range(26):
            dk = dist[k]
            for i in range(26):
                di = dist[i]
                ik = di[k]
                if ik == INF:
                    continue
                # try improve i->j via k
                for j in range(26):
                    nd = ik + dk[j]
                    if nd < di[j]:
                        di[j] = nd

        # sum required conversions
        total = 0
        for s_ch, t_ch in zip(source, target):
            if s_ch == t_ch:
                continue
            u = ord(s_ch) - ord('a')
            v = ord(t_ch) - ord('a')
            if dist[u][v] == INF:
                return -1
            total += dist[u][v]

        return total