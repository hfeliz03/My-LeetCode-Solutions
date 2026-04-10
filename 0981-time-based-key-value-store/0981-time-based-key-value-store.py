from collections import defaultdict
import heapq
class TimeMap:

    def __init__(self):
        self.timeMap = defaultdict(list)
        #put on each key a heap

    def set(self, key: str, value: str, timestamp: int) -> None:
        heapq.heappush(self.timeMap[key], [timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        #binary search on the timestamps at the given key.
        listOfTimeStamps = self.timeMap[key] #[[timeStamp1, val1], [timeStamp2, val2], ...]
        n = len(listOfTimeStamps)
        if n == 0 : return ""
        l, r = 0, n - 1
        prevTimeStamp = ""
        while l <= r:
            mid = (l+r) // 2
            if listOfTimeStamps[mid][0] == timestamp: return listOfTimeStamps[mid][1]
            elif listOfTimeStamps[mid][0] > timestamp:
                r = mid -1
            else: 
                l = mid + 1
                prevTimeStamp = listOfTimeStamps[mid][1]
        return prevTimeStamp



# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)