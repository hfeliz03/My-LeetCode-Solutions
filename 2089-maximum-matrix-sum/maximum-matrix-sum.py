class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        total = 0
        neg_count = 0
        min_abs = float('inf')

        for row in matrix:
            for x in row:
                total += abs(x)
                if x < 0:
                    neg_count += 1
                min_abs = min(min_abs, abs(x))

        # If odd # of negatives, one value must remain negative
        if neg_count % 2 == 1:
            total -= 2 * min_abs

        return total