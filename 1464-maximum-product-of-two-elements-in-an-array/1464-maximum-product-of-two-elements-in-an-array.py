class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        #Either the two biggest nums
        #or the two smallest nums
        nums.sort()
        return max((nums[-1]-1)*(nums[-2]-1), (nums[0]-1)*(nums[1]-1))