class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        if n == 1: 
            if nums[0] == target:
                return [0,0]
        elif n == 0: return [-1,-1]
        #elif target not in set(nums): return [-1,-1]
        
        l, r = 0, n-1

        foundTarget = -1
        # while l < r:
        #     mid = (r + l) // 2
        #     print(mid)
        #     if nums[mid] == target:
        #         foundTarget = mid
        #         break
        #     elif nums[mid] > target:
        #         r = mid - 1
        #     else:
        #         l = mid + 1
        
        left = foundTarget
        print(f'{l=}, {r=}')
        while l <= r:
            mid = (r + l) // 2
            if nums[mid] == target:
                if foundTarget == -1: foundTarget = mid
                left = mid
            if nums[mid] >= target:
                r = mid - 1
            else:
                l = mid + 1
        print(left)

        if foundTarget == -1: return [-1,-1]
        # print(foundTarget)
        print(f'{l=}, {r=}')
        l = foundTarget
        r = n-1
        right = foundTarget
        while l <= r:
            mid = (r + l) // 2
            if nums[mid] == target:
                right = mid
            if nums[mid] <= target:
                l = mid + 1
            else:
                r = mid - 1
        print(right)
        return [left, right]
