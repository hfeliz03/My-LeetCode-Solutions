class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        res = set()
    
        for i in range(len(nums)):
            target = -nums[i] 
            seen = set()
            
            for j in range(i + 1, len(nums)):
                needed = target - nums[j]
                if needed in seen:
                    triplet = tuple(sorted((nums[i], nums[j], needed)))
                    res.add(triplet)
                seen.add(nums[j])
        
        return [list(triplet) for triplet in res]