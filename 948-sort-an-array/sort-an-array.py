class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(l, r):
            li, ri = 0, 0
            res = []
            while li < len(l) and ri < len(r):
                if l[li] <= r[ri]:
                    res.append(l[li])
                    li += 1
                else:
                    res.append(r[ri])
                    ri += 1
            if li < len(l):
                res += l[li:]
            if ri < len(r):
                res += r[ri:]
            return res


        def mergesort(nums):
            if len(nums) <= 1: return nums
            n = len(nums) // 2
            l = mergesort(nums[:n])
            r = mergesort(nums[n:])
            return merge(l, r)
        
        return mergesort(nums)
