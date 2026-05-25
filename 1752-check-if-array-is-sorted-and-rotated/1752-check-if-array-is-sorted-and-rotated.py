class Solution:
    def check(self, nums: List[int]) -> bool:
        n = len(nums)
        saddle = 0
        for i in range(n-1):
            if nums[i] > nums[i+1]:
                saddle = i + 1
                break

        i = 0
        while i < n-1:
            if nums[(i + saddle) % n] > nums[(i + saddle + 1) % n]:
                return False
            i+=1

        return True 
