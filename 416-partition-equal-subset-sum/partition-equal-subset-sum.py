class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        setSums = set()
        setSums.add(0)
        sumNums = sum(nums)
        if sumNums % 2 != 0: 
            return False
        target = sumNums / 2
        for i in nums:
            toAdd = set()
            for sumi in setSums:
                toAdd.add(i+sumi)
            setSums = setSums.union(toAdd)
            print(setSums)
            if target in setSums:
                return True
        
        return False
