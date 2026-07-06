class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        res = set((x,y) for x,y in intervals)
        intervals.sort(key=lambda x: (x[0], -x[1]))
        n = len(intervals)
        print(intervals)
        i = 0
        j = 1
        while i < n:
            c, d = intervals[i]
            if i + j < n:
                if c <= intervals[i+j][0] and intervals[i+j][1] <= d:
                    res.remove((intervals[i+j][0], intervals[i+j][1]))
                    j += 1
                    continue
            print(f"{i=}, {c=}, {d=}")
            i += j
            j = 1
        print(res)
        return len(res)
