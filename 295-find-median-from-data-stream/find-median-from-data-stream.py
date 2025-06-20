class MedianFinder:

    def __init__(self):
        #Creation of max heap small and min heap large
        self.small , self.large = [], []

    def addNum(self, num: int) -> None:
        #IMPORTANT REMINDER: Python only implements min-heap.
        heapq.heappush(self.small, -1*num)

        if(self.small and self.large and (-1*self.small[0] > self.large[0])): heapq.heappush(self.large, -heapq.heappop(self.small))

        if len(self.small) - len(self.large) > 1 : heapq.heappush(self.large, -heapq.heappop(self.small))
        elif len(self.large) - len(self.small) > 1: heapq.heappush(self.small, -heapq.heappop(self.large))
        

    def findMedian(self) -> float:
        if len(self.small) > len(self.large): return -self.small[0]
        elif len(self.large) > len(self.small): return self.large[0]
        return (-self.small[0]+self.large[0])/2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()