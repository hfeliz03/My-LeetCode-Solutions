class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        # 1, 2, 2 = 3
        # 1, 2, 2, 2 = 3+4
        # 1, 2, 2, 2, 1, 2 = 3 + 4 + 6
        # res = 0
        # majority = 0
        # for i, val in enumerate(nums):
        #     if val == target: 
        #         majority += 1
        #     res += i+1 if majority > (i+1)/2 else 0
        # return res

        res = 0
        for i, val in enumerate(nums):
            count = 0
            for j, val2 in enumerate(nums[i:]):
                if val2 == target: count += 1
                if count > (j+1) / 2: 
                    res += 1

        return res