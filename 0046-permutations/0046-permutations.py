class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        #based on the lefting subarray, call a recursive function on all the possible numbers
        #once your length is n append that subarray to the result
        res = []

        def permute(curArr, subArr):
            if len(curArr) == len(nums) or not subArr: #lowkey the same conditions
                res.append(curArr)
                return 
            i = 0 
            while i < len(subArr):
                permute(curArr + [subArr[i]], subArr[:i] + subArr[i+1:])
                i+=1

        permute([], nums)
        return res