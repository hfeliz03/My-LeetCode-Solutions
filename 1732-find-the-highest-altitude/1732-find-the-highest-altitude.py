class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        highest = 0
        prev = 0
        for i, val in enumerate(gain):
            prev = val + prev
            highest = max(highest, prev)

        return highest