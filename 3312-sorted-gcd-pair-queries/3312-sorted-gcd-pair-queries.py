#This is pure insanity i Genuinely didnt even understand the explanation yet
class Solution:
    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
        mx = max(nums)

        arr = [0] * (mx + 1)
        for n in nums: arr[n] += 1

        for i in range(1, mx + 1): 
            for j in range(i * 2, mx + 1, i):
                arr[i] += arr[j]

        for i in range(1, mx + 1):
            arr[i] = arr[i] * (arr[i] - 1) // 2

        for i in range(mx, 0, -1):
            for j in range(i * 2, mx + 1, i):
                arr[i] -= arr[j]

        for i in range(1, mx + 1):
            arr[i] += arr[i - 1]
        
        res = []
        for q in queries: 
            idx = bisect.bisect_left(arr, q + 1)
            res.append(idx)
        
        return res
