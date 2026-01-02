class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        numsSet = set(nums)
        disappeared = []
        for i in range(1,len(nums)+1):
            if i not in numsSet:
                disappeared.append(i)
        
        print(numsSet)
        print(disappeared)
        return disappeared