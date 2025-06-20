class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if not stones : return 0
        stonesMaxHeap = [-stones for stones in stones]
        heapq.heapify(stonesMaxHeap)

        while len(stonesMaxHeap) > 1:
            y, x = -heapq.heappop(stonesMaxHeap), -heapq.heappop(stonesMaxHeap)
            if y == x: continue
            if y > x: heapq.heappush(stonesMaxHeap, -(y-x))
        return -stonesMaxHeap[0] if stonesMaxHeap else 0

            