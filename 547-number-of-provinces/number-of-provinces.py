class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        # The diagonal of the matrix is always 1
        # Below the diagonal == above the diagonal mirrored. WE CAN SKIP CHECKING THIS
        # Return the number of Connected Components (provinces)
        # The More connected components that we have, the more provinces. Thus if we find out that two components are connected, the number of provinces decrease
        # isConnected will always be a squared matrix
        # 1 0 0 1
        # 0 1 1 0
        # 0 1 1 1
        # 1 0 1 1
        # 0->3 1->2 2->3 
        # 0->3 3->2 2->1
        # for row in isConnected:
        #     print(row)
        # print()
        provinces = len(isConnected)
        connected = [i for i in range(provinces)]

        def dfs(row, component):
            j = 0
            while j < len(isConnected):
                if isConnected[row][j] == 1 and row != j:
                    isConnected[row][j] = 0
                    isConnected[j][row] = 0
                    connected[row] = component
                    connected[j] = component
                    dfs(j, component)
                j+=1
            return 

        
        i = 0
        while i < len(isConnected) and provinces > 1:
            if connected[i] == i: #Is not explored by any other node previously
                dfs(i,i)
            i+=1

        print(connected)
        diffComponents = set(connected)
        return len(diffComponents)
