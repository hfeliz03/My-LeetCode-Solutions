class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adjList = {}
        visited = set()
        toVisit = set(element for element in range(n))
        comps = 0

        if len(edges) == 0: return comps
        
        for x,y in edges:
            adjList[x] = adjList.get(x, set())
            adjList[x].add(y)
            adjList[y] = adjList.get(y, set())
            adjList[y].add(x)

        def bfs(neighbors):
            while neighbors:
                cur = neighbors.pop()
                toVisit.discard(cur)
                visited.add(cur)
                for element in adjList[cur]: 
                    if element not in visited:
                        neighbors.add(element) 

        while toVisit:
            curNode = toVisit.pop()
            visited.add(curNode)
            if curNode in adjList:
                neighbors = adjList[curNode]
                bfs(neighbors)
            comps += 1

        return comps