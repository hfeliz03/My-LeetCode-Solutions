from collections import Counter, defaultdict
class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        #These relationships are not always reciprocal
        res = []
        n, m = len(nums), len(queries)

        indices = defaultdict(list)
        for i, num in enumerate(nums):
            indices[num].append(i)
        
        
        for i in range(m):
            val = nums[queries[i]]
            indicesOfVal = indices[val]
            m = len(indicesOfVal)
            targetIndex = queries[i]
            if m == 1: 
                res.append(-1)
                
            else:
                # I have to find the index where i have stored queries[i] on at indices[target], such that i can look one forward and one backwards
                l, r = 0, m-1
                targetIndexAtIndicesOfVal = -1
                while l <= r:
                    mid = (l + r) // 2
                    if indicesOfVal[mid] == targetIndex: 
                        targetIndexAtIndicesOfVal = mid
                        break
                    elif indicesOfVal[mid] > targetIndex: r = mid - 1
                    else: l = mid + 1
                distForward = (n - targetIndex + indicesOfVal[(targetIndexAtIndicesOfVal + 1) % m]) % n
                distBackward = (n + targetIndex - indicesOfVal[(targetIndexAtIndicesOfVal - 1 + m) % m]) % n
                minDist = min(distForward, distBackward)
                res.append(minDist)
        return res
            

        

        