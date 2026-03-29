class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        #I want to maximize the number of intervals, because big intervals steal space for other intervals to be there.
        #Earliest finish time
        intervals.sort(key = lambda x: x[1] )
        count = 1
        curEnd = intervals[0][1]
        for interval in intervals[1:]:
            if interval[0] < curEnd:
                continue
            else: #Start of new interval is after/right after, the current finish time
                curEnd = interval[1]
                count+=1

        return len(intervals) - count