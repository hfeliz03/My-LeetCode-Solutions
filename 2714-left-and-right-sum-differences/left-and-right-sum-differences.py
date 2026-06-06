class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        n = len(nums)
        sumL, sumR = [0]*n, [0]*n
        print(sumL)
        print(sumR)
        print()
        for i in range(1,n):
            sumL[i] = sumL[i-1] + nums[i-1]
            sumR[-i-1] = sumR[-i] + nums[-i]
        print(sumL)
        print(sumR)
        return [abs(sumL[i] - sumR[i]) for i in range(n)]