class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # I have some amount of numbers
        # i must create the power set
        subsets = [[]]
        # [4], [1,4], [2,4], [1,2,4], [3,4], [1,3,4], [2,3,4], [1,2,3,4]
        for num in nums:
            curSubsetsAtNum = []
            for curSubset in subsets:
                #update curSubsetsAtNum
                curSubsetsAtNum.append(curSubset + [num])
            subsets += curSubsetsAtNum
        
        #print(subsets)
        return subsets