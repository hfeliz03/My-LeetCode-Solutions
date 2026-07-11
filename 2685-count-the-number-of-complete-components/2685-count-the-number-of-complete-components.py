class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]

        for x, y in edges:
            adj[x].append(y)
            adj[y].append(x)

        visited = set()
        complete_components = 0

        def dfs(node):
            visited.add(node)
            component = [node]

            for neighbor in adj[node]:
                if neighbor not in visited:
                    component.extend(dfs(neighbor))

            return component

        for node in range(n):
            if node in visited:
                continue

            component = dfs(node)
            component_size = len(component)

            if all(len(adj[x]) == component_size - 1 for x in component):
                complete_components += 1

        return complete_components