class Solution:
    def check(self, nums: List[int]) -> bool:
        dec = False
        n = len(nums)
        turningPoint = 0
        for i in range(n-1):
            if nums[i] > nums[i+1]:
                turningPoint = i + 1
                break
        print(turningPoint)
        i = 0
        while i < n-1:
            print(f"Comparisons = {nums[(i + turningPoint) % n]} and {nums[(i + turningPoint + 1) % n]}")
            if nums[(i + turningPoint) % n] > nums[(i + turningPoint + 1) % n]:
                return False
            i+=1

        return True 
