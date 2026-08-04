class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff = {} 
        for i, num in enumerate(nums):
            diff[target-num] = i

        for i, num in enumerate(nums):
            if num in diff.keys() and  i != diff[num]:
                return [i, diff[num]]
        return