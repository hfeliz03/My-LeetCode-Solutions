class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        for ast in sorted(asteroids):
            if mass < ast: return False
            mass += ast
        return True