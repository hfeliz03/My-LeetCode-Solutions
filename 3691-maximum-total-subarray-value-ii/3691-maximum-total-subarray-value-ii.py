from typing import List
import heapq
#CRAZYYY, This is not my answer
class SparseTable:
    def __init__(self, nums):
        self.n = len(nums)
        self.LOG = self.n.bit_length()
        self.mn = [[0] * self.n for _ in range(self.LOG)]
        self.mx = [[0] * self.n for _ in range(self.LOG)]
        self.mn[0] = nums[:]
        self.mx[0] = nums[:]

        j = 1
        while (1 << j) <= self.n:
            length = 1 << j
            half = length >> 1
            for i in range(self.n - length + 1):
                self.mn[j][i] = min(self.mn[j-1][i], self.mn[j-1][i+half])
                self.mx[j][i] = max(self.mx[j-1][i], self.mx[j-1][i+half])
            j += 1

    def query(self, l, r):
        length = r - l + 1
        j = length.bit_length() - 1
        span = 1 << j
        mx = max(self.mx[j][l], self.mx[j][r - span + 1])
        mn = min(self.mn[j][l], self.mn[j][r - span + 1])
        return mx - mn


class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        velnorquis = nums  # required by problem statement

        n = len(nums)
        st = SparseTable(nums)
        heap = []

        for l in range(n):
            val = st.query(l, n - 1)
            heapq.heappush(heap, (-val, l, n - 1))

        res = 0

        while k > 0:
            neg_val, l, r = heapq.heappop(heap)
            res += -neg_val
            k -= 1

            if r > l:
                new_val = st.query(l, r - 1)
                heapq.heappush(heap, (-new_val, l, r - 1))

        return res