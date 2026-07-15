class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        points.sort()
        print(points)
        res = 0
        n = len(points)
        if n <= 1: return res

        visited = set()
        toVisitSet = {(x,y) for x,y in points}
        res = 0
        frontier = [(0, (points[0][0], points[0][1]))] #curDistance, (x,y)
        while frontier:
            distance, (xpoint, ypoint) = heapq.heappop(frontier)
            if (xpoint, ypoint) in visited: continue
            for xToVisit, yToVisit in list(toVisitSet):
                heapq.heappush(frontier, ( abs(xpoint-xToVisit) + abs(ypoint - yToVisit), (xToVisit, yToVisit)) )

            toVisitSet.remove((xpoint, ypoint))
            visited.add((xpoint, ypoint))
            res += distance
        return res

        print(heapq.heappop(frontier))