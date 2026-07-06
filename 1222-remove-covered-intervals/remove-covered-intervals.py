class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[0], -x[1]))

        res = len(intervals)
        i = 0
        n = len(intervals)

        while i < n:
            c, d = intervals[i]
            j = i + 1

            while j < n and c <= intervals[j][0] and intervals[j][1] <= d:
                res -= 1
                j += 1

            i = j

        return res