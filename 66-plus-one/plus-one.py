class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        i = len(digits)-1
        while i >= 0 and carry == 1:
            digits[i] += 1
            if digits[i]>9: 
                digits[i] = 0
                if i==0: digits = [1]+digits 
            else: carry = 0
            i -= 1
        return digits