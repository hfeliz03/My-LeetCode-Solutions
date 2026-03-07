class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        # # The diagonal of the matrix is always 1
        # # Below the diagonal == above the diagonal mirrored. WE CAN SKIP CHECKING THIS
        # # Return the number of Connected Components (provinces)
        # # The More connected components that we have, the more provinces. Thus if we find out that two components are connected, the number of provinces decrease
        # # isConnected will always be a squared matrix


        n = len(isConnected)
        visited = [False] * n
        provinces = 0

        def dfs(city):
            for neighbor in range(n):
                if isConnected[city][neighbor] == 1 and not visited[neighbor]:
                    visited[neighbor] = True
                    dfs(neighbor)

        for city in range(n):
            if not visited[city]:
                provinces += 1
                visited[city] = True
                dfs(city)

        return provinces
        # connected = [i for i in range(len(isConnected))]

        # def dfs(row, component):
        #     j = 0
        #     while j < len(isConnected):
        #         if isConnected[row][j] == 1 and row != j:
        #             isConnected[row][j] = 0
        #             isConnected[j][row] = 0
        #             connected[j] = component
        #             dfs(j, component)
        #         j+=1
        #     return 

        
        # i = 0
        # while i < len(isConnected):
        #     if connected[i] == i: #Is not explored by any other node previously

        #         dfs(i,i)
        #     i+=1

        # diffComponents = set(connected)
        # return len(diffComponents)
