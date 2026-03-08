class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        if len(nums) == 1:
            if nums[0] == "0": return "1"
            else: return "0"
            
        binaries = []
        for i in range(len(nums[0]) ** 2):
            binaries.append(f"{i:0{len(nums[0])}b}")

        difference = set(binaries).difference(set(nums))
        return difference.pop() if difference else 0
                