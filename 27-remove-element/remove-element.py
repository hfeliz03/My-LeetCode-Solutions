class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        numRemains, index = len(nums)-1, 0
        while index <= numRemains:
            if nums[index] == val:
                nums[index], nums[numRemains] = nums[numRemains], nums[index]
                numRemains-= 1
                continue
            index +=1
        print(nums)
        return numRemains+1