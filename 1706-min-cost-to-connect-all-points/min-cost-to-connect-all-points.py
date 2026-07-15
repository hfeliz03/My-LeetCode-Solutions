class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        res = 0
        n = len(points)
        if n <= 1: return res

        visited = set()
        frontier = [(0, (points[0][0], points[0][1]))] #curDistance, (x,y)
        pointsSet = set([(x,y) for x,y in points])
        while frontier:
            distance, (xpoint, ypoint) = heapq.heappop(frontier)
            if (xpoint, ypoint) in visited: continue
            for xToVisit, yToVisit in list(pointsSet - visited):
                heapq.heappush(frontier, ( abs(xpoint-xToVisit) + abs(ypoint - yToVisit), (xToVisit, yToVisit)) )

            visited.add((xpoint, ypoint))
            res += distance
        return res
