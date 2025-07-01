class Solution:
    def theMaximumAchievableX(self, num: int, t: int) -> int:
        if t < 1 : return num
        return num + t * 2 