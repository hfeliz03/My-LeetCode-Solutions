class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        
        nums1Sorted = sorted(nums1)
        #all even:
        valid = False
        for i, numi in enumerate(nums1):
            if numi % 2 == 0: valid = True
            else: #get a number smaller than num and that changes its parity
                for numj in nums1Sorted:
                    if numj % 2 == 1 and numi != numj and numi - numj >= 1: 
                        valid = True
                        break
            if not valid: 
                break

            if i != len(nums1) - 1: valid = False
        
        if valid : return True

        #all odd:
        for i, numi in enumerate(nums1):
            if numi % 2 == 1: valid = True
            else: 
                for numj in nums1Sorted:
                    if numj % 2 == 1 and numi != numj and numi - numj >= 1: 
                        valid = True
                        break
            if not valid: 
                break

            if i != len(nums1) - 1: valid = False
        
        return valid
        

