class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i0 = -1
        for i in range(len(nums)):
            if nums[i] == 0:
                nums[i0+1], nums[i] = nums[i], nums[i0+1]
                i0 += 1
        i1 = i0+1
        for i in range(i1,len(nums)):
            if nums[i] == 1:
                nums[i1], nums[i] = nums[i], nums[i1]
                i1 += 1

        # 0 0 2 1 1 2
