class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        if not nums: return True
        def helper(curNums:List[int], p1:int, p2: int, p1Turn:bool):
            print(f"{curNums=}, {p1=}, {p2=}, {p1Turn=}")
            if not curNums:
                if p1 >= p2: return True
                else: return False
            if p1Turn == True:
                return helper(curNums[:-1], p1+curNums[-1], p2, False) or helper(curNums[1:], p1+curNums[0], p2, False) 
            else:
                return helper(curNums[:-1], p1, p2+curNums[-1], True) and helper(curNums[1:], p1, p2+curNums[0], True) 
        

        return helper(nums[:-1], nums[-1], 0, False) or helper(nums[1:], nums[0], 0, False)
            