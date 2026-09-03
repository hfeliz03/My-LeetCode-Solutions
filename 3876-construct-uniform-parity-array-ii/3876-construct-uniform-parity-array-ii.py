class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        nums2Even = []
        nums1Sorted = sorted(nums1)
        #all even:
        for i, numi in enumerate(nums1):
            if numi % 2 == 0: nums2Even.append(numi)
            else: #get a number smaller than num and that is odd
                for numj in nums1Sorted:
                    if numj % 2 == 1 and numi != numj and numi - numj >= 1: 
                        nums2Even.append(numi - numj)
                        break
            if len(nums2Even) == i: 
                nums2Even = [] #couldnt find a number that fulfils our condition"
                break
        

        nums2Odd = []
        #all odd:
        for i, numi in enumerate(nums1):
            if numi % 2 == 1: nums2Odd.append(numi)
            else: #get a number smaller than num and that is even
                for numj in nums1Sorted:
                    if numj % 2 == 1 and numi != numj and numi - numj >= 1: 
                        nums2Odd.append(numi - numj)
                        break
            if len(nums2Odd) == i: 
                nums2Odd = [] #couldnt find a number that fulfils our condition"
                break
        
        print(nums2Even)
        print(nums2Odd)
        return True if nums2Odd or nums2Even else False
        

