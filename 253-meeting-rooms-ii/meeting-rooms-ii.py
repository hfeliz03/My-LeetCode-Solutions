class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        # Sort 
        # Start traversing the intervals
        # If at some point you find conflicting meetings, start a new branch
        # Keep the concurrent finishing times in an array
        # return the length of that array
        if not intervals: return 0
        intervals.sort()
        currFinishingTimes = [intervals[0][1]]
        for i in intervals[1:]:
            needNewRoom = True
            for j in range(len(currFinishingTimes)):
                if i[0] >= currFinishingTimes[j]: 
                    currFinishingTimes[j] = i[1] # that room can be used for the new meeting i
                    needNewRoom = False
                    break

            if needNewRoom == True: currFinishingTimes.append(i[1]) # if the start of an interval is smaller than the end of all others on-goning, we have a conflict, need to use a new room


        return len(currFinishingTimes)