class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        res = 0
        for num in arr1:
            valid = True
            for num2 in arr2:
                if abs(num - num2) <= d: 
                    valid = False
                    break
            if valid: res += 1
        
        return res
