from collections import Counter
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        ctr = Counter(arr)
        print(ctr.values())
        return len(set(arr)) == len(set(ctr.values()))