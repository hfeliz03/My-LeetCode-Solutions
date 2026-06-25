class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        subsets = {()}
        nums.sort()

        for num in nums:
            newSubsets = set()

            for cur in subsets:
                newSubsets.add(cur + (num,))

            for subset in newSubsets: subsets.add(subset)

        return list(subsets)