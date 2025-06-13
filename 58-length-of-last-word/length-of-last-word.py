class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        arr = s.strip().split(" ")
        print(arr)
        return len(arr[-1])