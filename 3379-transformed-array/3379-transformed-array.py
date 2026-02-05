class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = []

        for i in range(n):
            if nums[i] < 0:
                result.append( nums[(i - abs(nums[i])) % n ])
            elif nums[i] > 0:
                result.append( nums[(i + nums[i]) % n])
            else:
                result.append(nums[i])
        
        return result