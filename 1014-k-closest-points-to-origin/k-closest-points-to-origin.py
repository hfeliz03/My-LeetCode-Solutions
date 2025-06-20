class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        if not points or k <= 0: return []
        max_heap = []
        
        for point in points:
            x, y = point
            heapq.heappush(max_heap, (-(x**2 + y**2) , point))
            if len(max_heap) > k: heapq.heappop(max_heap)

        # Extract points from the heap
        return [point for (_, point) in max_heap]