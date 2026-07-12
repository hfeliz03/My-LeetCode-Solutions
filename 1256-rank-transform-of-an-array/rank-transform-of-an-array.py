class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        if not arr: return []
        n = len(arr)
        ranks = [None] * n
        sortedArr = sorted(arr)
        dicArr = {}
        i = 0
        for val in sortedArr:
            if val not in dicArr:
                dicArr[val] = i
            else: 
                i -= 1
            i += 1

        for i in range(n):
            ranks[i] = dicArr[arr[i]] + 1
        return ranks