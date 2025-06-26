class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) <= 1 : return intervals 
        res = []
        # Sort intervals by their start time
        intervals.sort(key=lambda x: x[0])
        res = [intervals[0]]

        for i in range(1, len(intervals)):
            last = res[-1]
            current = intervals[i]

            # If curr overlaps with prev, merge them
            if current[0] <= last[1]: last[1] = max(last[1], current[1])
            else: res.append(current)

        return res