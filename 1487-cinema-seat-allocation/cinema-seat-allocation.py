class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        rows = defaultdict(set)
        for r, c in reservedSeats:
            rows[r].add(c)

        ans = 2 * n

        for seats in rows.values():
            left = {2,3,4,5}.isdisjoint(seats)
            right = {6,7,8,9}.isdisjoint(seats)
            middle = {4,5,6,7}.isdisjoint(seats)

            if left and right: continue
            elif left or right or middle: ans -= 1
            else: ans -= 2

        return ans