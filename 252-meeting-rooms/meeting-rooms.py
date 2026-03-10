class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        #check if there is no overlap in any of the i's 
        #Sort
        #Get a variable with the currFinish time, if currFinish > nextMeetingStart. Then False
        if not intervals: return True
        intervals.sort()
        curEnding = intervals[0][1]
        for i in intervals[1:]:
            if curEnding > i[0]: return False
            curEnding = i[1]
        return True
