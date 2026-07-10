class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        mapping = defaultdict(list)
        for i, num in enumerate(nums):
            mapping[num].append(i)
            if len(mapping[num]) > 1:
                if mapping[num][-1] - mapping[num][-2] <= k: return True
        return False
        