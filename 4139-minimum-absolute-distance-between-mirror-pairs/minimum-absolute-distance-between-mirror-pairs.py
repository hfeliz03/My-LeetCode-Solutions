from bisect import bisect_left
from collections import defaultdict
class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        revpos = defaultdict(list)
        def reverse(num):
            asStr = str(num)
            rev = ""
            for char in asStr:
                rev = char + rev
            return int(rev)
        
        for i, num in enumerate(nums):
            revpos[reverse(num)].append(i)
        
        print(revpos)
        minDis = 10**5
        for i, num in enumerate(nums):
            if num in revpos:
                arr = revpos[num]   # sorted list of indices
                pos = bisect_left(arr, i)

                # check left neighbor
                if pos - 1 >= 0:
                    j = arr[pos - 1]
                    if i > j:
                        minDis = min(minDis, abs(i - j))
                    
        return minDis if minDis != 10**5 else -1