class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums_minHeap = nums
        heapq.heapify(self.nums_minHeap)
        while len(self.nums_minHeap) > self.k:
            heapq.heappop(self.nums_minHeap)
        
    def add(self, val: int) -> int:
        heapq.heappush(self.nums_minHeap, val)
        if len(self.nums_minHeap) > self.k:
            heapq.heappop(self.nums_minHeap)
        return self.nums_minHeap[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)