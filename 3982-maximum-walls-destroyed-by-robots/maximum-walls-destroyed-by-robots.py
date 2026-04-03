from bisect import bisect_left, bisect_right
from typing import List
#I didnt solve this on my own, some Hards are genuinely ridiculous
class Solution:
    def maxWalls(self, robots: List[int], distance: List[int], walls: List[int]) -> int:
        pairs = sorted(zip(robots, distance))
        r = [p for p, _ in pairs]
        d = [dist for _, dist in pairs]
        n = len(r)

        walls.sort()
        wall_set = set(walls)

        def count_closed(lo: int, hi: int) -> int:
            if lo > hi:
                return 0
            return bisect_right(walls, hi) - bisect_left(walls, lo)

        # 1) Walls exactly at robot positions
        selfWall = [1 if r[i] in wall_set else 0 for i in range(n)]

        # 2) Outer intervals (exclude robot's own position)
        outerLeft = count_closed(r[0] - d[0], r[0] - 1)
        outerRight = count_closed(r[-1] + 1, r[-1] + d[-1])

        # 3) Internal gaps: only strict walls between consecutive robots
        rightCnt = [0] * (n - 1)
        leftCnt = [0] * (n - 1)
        unionCnt = [0] * (n - 1)

        for i in range(n - 1):
            # walls strictly in (r[i], r[i+1])
            gap_lo = r[i] + 1
            gap_hi = r[i + 1] - 1

            # robot i shooting right
            right_reach = min(r[i] + d[i], r[i + 1] - 1)
            rc = count_closed(gap_lo, right_reach)

            # robot i+1 shooting left
            left_reach = max(r[i + 1] - d[i + 1], r[i] + 1)
            lc = count_closed(left_reach, gap_hi)

            # overlap of those two intervals
            overlap_lo = max(gap_lo, left_reach)
            overlap_hi = min(gap_hi, right_reach)
            overlap = count_closed(overlap_lo, overlap_hi)

            rightCnt[i] = rc
            leftCnt[i] = lc
            unionCnt[i] = rc + lc - overlap

        # 4) DP
        # Base: robot 0 always can destroy selfWall[0], plus outerLeft if it shoots left
        dpL = selfWall[0] + outerLeft
        dpR = selfWall[0]

        for i in range(n - 1):
            newL = selfWall[i + 1] + max(
                dpL + leftCnt[i],      # previous L, current L
                dpR + unionCnt[i]      # previous R, current L
            )
            newR = selfWall[i + 1] + max(
                dpL + 0,               # previous L, current R
                dpR + rightCnt[i]      # previous R, current R
            )
            dpL, dpR = newL, newR

        # Add right exterior only if last robot shoots right
        return max(dpL, dpR + outerRight)