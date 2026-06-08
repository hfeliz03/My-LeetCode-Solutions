class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        prior, equal, posterior = [],[],[]
        for num in nums:
            if num < pivot: prior.append(num)
            elif num == pivot: equal.append(num)
            else: posterior.append(num)
        return prior + equal + posterior