class Solution:
    def findMin(self, nums: List[int]) -> int:
        smallest, l, r = nums[0], 0, len(nums)-1
        
        while l <= r:
            mid = l+(r-l)//2 
            if smallest > nums[mid]:
                smallest = nums[mid]
                r = mid-1
            else:
                l = mid+1

        return smallest
