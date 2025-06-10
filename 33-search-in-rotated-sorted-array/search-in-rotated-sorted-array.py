class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums: return -1
        l , r = 0, len(nums)-1
        if nums[l] == target: return 0
        if nums[r] == target: return r
        
        while l < r:
            mid = l+(r-l)//2 
            if nums[mid] > nums[r]:
                l = mid+1
            else:
                r = mid
        k = l
    
        
        l , r = 0, (len(nums)-1)
        
        while l <= r:
            mid = (l+r)//2
            real_mid = (mid+k) % len(nums)
            if nums[real_mid] == target: return real_mid
            if  nums[real_mid] > target:
                r = mid-1
            else:
                l = mid+1
        return -1

