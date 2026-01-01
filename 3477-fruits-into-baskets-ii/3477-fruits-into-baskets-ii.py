class Solution(object):
    def numOfUnplacedFruits(self, fruits, baskets):
        """
        :type fruits: List[int]
        :type baskets: List[int]
        :rtype: int
        """
        unplaced = 0
        for fruit in fruits:
            placed = False
            for i, basket in enumerate(baskets):
                if basket >= fruit:
                    baskets.pop(i)
                    placed = True
                    break
            if not placed:
                unplaced += 1
            
        return unplaced