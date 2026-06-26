#Did not solve this myself. Had to give up
from typing import List

class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        n = len(nums)

        # prefix sum ranges from -n to n, so shift by n+1
        size = 2 * n + 3
        offset = n + 1
        bit = [0] * (size + 1)

        def add(i, delta):
            while i <= size:
                bit[i] += delta
                i += i & -i

        def query(i):
            s = 0
            while i > 0:
                s += bit[i]
                i -= i & -i
            return s

        res = 0
        prefix = 0

        # prefix[0] = 0
        add(prefix + offset, 1)

        for x in nums:
            prefix += 1 if x == target else -1

            # count previous prefixes smaller than current prefix
            res += query(prefix + offset - 1)

            add(prefix + offset, 1)

        return res