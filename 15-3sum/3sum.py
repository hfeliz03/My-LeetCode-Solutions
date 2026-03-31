class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        res = []
        
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            l, r = i + 1, len(nums) - 1
            
            while l < r:
                total = nums[i] + nums[l] + nums[r]
                
                if total < 0:
                    l += 1
                elif total > 0:
                    r -= 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
        
        return res
        # res = set()
    
        # for i in range(len(nums)):
        #     target = -nums[i] 
        #     seen = set()
            
        #     for j in range(i + 1, len(nums)):
        #         needed = target - nums[j]
        #         if needed in seen:
        #             triplet = tuple(sorted((nums[i], nums[j], needed)))
        #             res.add(triplet)
        #         seen.add(nums[j])
        
        # return [list(triplet) for triplet in res]