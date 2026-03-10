import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # 6 3 5 2 1 4
        # 5 3 4 2 1 
        # 1 5 3 -3
        # -5 -3 -1 3
        # This is a minHeap
        # To use it as a maxHeap, negate the values.
        # Pop k-1 values, return kth or -heap.peek
        # if k > len(nums): return 0
        # myHeap = []
        # for num in nums:
        #     heapq.heappush(myHeap, -num)
        # for _ in range(k-1):
        #     heapq.heappop(myHeap)
        # return -myHeap[0]
        if k > len(nums): return 0
        myHeap = []
        for num in nums:
            heapq.heappush(myHeap, num)
            if len(myHeap) > k:
                heapq.heappop(myHeap)
        return myHeap[0]