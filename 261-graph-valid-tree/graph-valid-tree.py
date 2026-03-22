class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1: return False
        if len(edges) == 0 and n == 1: return True
        adjList = dict()
        for edge in edges:
            u, v = edge
            adjList[u], adjList[v] = adjList.get(u, set()), adjList.get(v, set()) 
            adjList[u].add(v)
            adjList[v].add(u)
        
        visited = set()
        if 0 in adjList: queue = [0] 
        else: return False
        
        while queue:
            curNode = queue.pop()
            for neighbor in list(adjList[curNode]):
                if neighbor in visited: return False
                queue.append(neighbor)
                adjList[neighbor].remove(curNode)
            visited.add(curNode)

        return True if len(visited) == n else False
