class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        setSums = {0}
        sumNums = sum(nums)
        if sumNums % 2 != 0: return False
        target = sumNums / 2
        for i in nums:
            toAdd = set()
            for sumi in setSums:
                toAdd.add(i+sumi)
            setSums = setSums.union(toAdd)
            if target in setSums: return True
        
        return False
