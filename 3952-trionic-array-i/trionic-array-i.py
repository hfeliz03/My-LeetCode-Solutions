class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        p, q = -1, -1
        for i in range(1, len(nums)):
            if (nums[i] < nums[i-1]) and (p == -1 )and (i-1 != 0):
                p = i-1
                print("1")
            elif nums[i] > nums[i-1] and p != -1 and q == -1:
                q = i
                print("2")
            elif nums[i] > nums[i-1] and ((p == -1 and q == -1) or (p != -1 and q != -1)):
                print("3")
                continue
            elif nums[i] < nums[i-1] and p != -1 and q == -1:
                print("4")
                continue
            else:
                return False
        return p != -1 and q != -1