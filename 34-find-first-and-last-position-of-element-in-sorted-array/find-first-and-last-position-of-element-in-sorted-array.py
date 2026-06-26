class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        
        l, r = 0, n-1

        foundTarget = -1
        
        left = foundTarget
        while l <= r:
            mid = (r + l) // 2
            if nums[mid] == target:
                if foundTarget == -1: foundTarget = mid
                left = mid
            if nums[mid] >= target:
                r = mid - 1
            else:
                l = mid + 1

        if foundTarget == -1: return [-1,-1]

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
        return [left, right]
