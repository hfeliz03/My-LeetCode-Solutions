import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # ui -> vi
        # graph => source: [[sink, time], [sink2, time2]]
        # minHeap = [time, node]
        graph = defaultdict(list)
        for ui, vi, wi in times:
            graph[ui].append([vi, wi])

        minHeap = [[0, k]]
        bestTime = {}
        while minHeap:
            curTime, curNode = heapq.heappop(minHeap)
            if curNode in bestTime: continue
            bestTime[curNode] = curTime
            print(bestTime)
            
            
            for neighbor, time in graph[curNode]:
                if neighbor in bestTime: continue #best path for that neighbor was already found
                heapq.heappush(minHeap, [curTime + time, neighbor])
        
        return max(bestTime.values()) if len(bestTime) == n else -1

