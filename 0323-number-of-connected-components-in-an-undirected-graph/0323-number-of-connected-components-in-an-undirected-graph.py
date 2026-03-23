class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adjList = {}
        toVisit = set(range(n))
        comps = 0

        for x, y in edges:
            adjList.setdefault(x, set()).add(y)
            adjList.setdefault(y, set()).add(x)

        while toVisit:
            curNode = toVisit.pop()
            stack = [curNode]

            while stack:
                node = stack.pop()
                for nei in adjList.get(node, set()):
                    if nei in toVisit:
                        toVisit.remove(nei)
                        stack.append(nei)

            comps += 1

        return comps