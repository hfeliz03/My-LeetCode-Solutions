class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        highest = 0
        for i, val in enumerate(gain):
            gain[i] = val + gain[i-1] if i > 0 else val + highest
            highest = max(highest, gain[i])

        return highest