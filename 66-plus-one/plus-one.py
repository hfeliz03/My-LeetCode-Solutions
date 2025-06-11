class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if not digits: return None

        if digits[-1] != 9:
            digits[-1]+=1 
            return digits
        else:
            i = len(digits) - 1
            while i >= 0:
                if digits[i] >= 9:
                    digits[i] = 0
                else: 
                    digits[i] += 1
                    return digits
                i-=1

        return [1] + digits 