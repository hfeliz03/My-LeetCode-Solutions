class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums: return 0
        k = 1

        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]: #solve duplicate
                nums[k] = nums[i]
                k+=1 #non duplicate found

        return k
    
    