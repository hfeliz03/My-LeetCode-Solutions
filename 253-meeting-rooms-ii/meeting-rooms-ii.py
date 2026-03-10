class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        # Sort 
        # Start traversing the intervals
        # If at some point you find conflicting meetings, start a new branch
        # Keep the concurrent finishing times in an array
        # return the length of that array
        if not intervals: return 0
        intervals.sort()
        currFinishingTimes = []
        heapq.heappush(currFinishingTimes, intervals[0][1])
        for i in intervals[1:]:
            if i[0] >= currFinishingTimes[0]: 
                heapq.heappop(currFinishingTimes) 
            heapq.heappush(currFinishingTimes, i[1]) # if the start of an interval is smaller than the end of all others on-goning, we have a conflict, need to use a new room


        return len(currFinishingTimes)