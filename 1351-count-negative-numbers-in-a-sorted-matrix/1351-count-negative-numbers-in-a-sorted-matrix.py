class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count = 0
        for row in grid:
            rowSorted = sorted(row)
            for num in rowSorted:
                if num < 0: 
                    count += 1
                else:
                    break
        return count