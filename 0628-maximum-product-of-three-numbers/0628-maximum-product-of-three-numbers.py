class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        three_largest = nums[-1] * nums[-2] * nums[-3]
        two_smallest_and_largest = nums[0] * nums[1] * nums[-1]

        return max(three_largest, two_smallest_and_largest)