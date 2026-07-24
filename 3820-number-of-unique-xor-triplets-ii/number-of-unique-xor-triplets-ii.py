class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        res = set()
        pairs = set()
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                pairs.add(nums[i] ^ nums[j])
        
        for val in pairs:
            for k in range(len(nums)):
                res.add(val ^ nums[k])

        return len(res)