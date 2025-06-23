class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        #"Shrink" the matrix layer by layer.
        spiralMtx = []
        l, r, t, b = 0, len(matrix[0]), 0, len(matrix)
        
        while l < r and t < b:
            #Cover top row:
            for i in range(l, r):
                spiralMtx.append(matrix[t][i])
            t += 1

            for i in range(t, b):
                spiralMtx.append(matrix[i][r-1])
            r -= 1

            if not(l<r and t<b): break
        
            for i in range(r - 1, l - 1, -1):
                spiralMtx.append(matrix[b-1][i])
            b-=1

            for i in range(b-1, t-1, -1):
                spiralMtx.append(matrix[i][l])
            l += 1
        return spiralMtx