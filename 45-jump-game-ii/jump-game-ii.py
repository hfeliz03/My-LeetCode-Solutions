class Solution:
    def jump(self, nums: List[int]) -> int:
        #Stop to jump on a new index, if that index can take you farther than your current max step
        jumps = 0
        i = 0
        n = len(nums)

        while i != n-1:
            jumps += 1
            if i + nums[i] >= n-1: return jumps
            
            bestReach = 0
            newI = i

            for j in range(1,nums[i]+1):
                candidate = i + j 

                if candidate < n:
                    reach = candidate + nums[candidate]

                    if reach > bestReach: 
                        bestReach = reach
                        newI = candidate
            i = newI
        return jumps