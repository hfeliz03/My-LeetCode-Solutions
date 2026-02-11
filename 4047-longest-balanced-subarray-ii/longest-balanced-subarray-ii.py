from typing import List
from collections import defaultdict

class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        n = len(nums)

        # Segment tree over indices [0..n]
        # We conceptually store prefix_sum[pos] for every pos.
        # We'll do range add updates and query earliest index with prefix_sum == target.

        size = 4 * (n + 1)
        mn = [0] * size
        mx = [0] * size
        lazy = [0] * size

        def apply(u: int, v: int):
            mn[u] += v
            mx[u] += v
            lazy[u] += v

        def push(u: int):
            if lazy[u] != 0:
                apply(u * 2, lazy[u])
                apply(u * 2 + 1, lazy[u])
                lazy[u] = 0

        def pull(u: int):
            mn[u] = min(mn[u * 2], mn[u * 2 + 1])
            mx[u] = max(mx[u * 2], mx[u * 2 + 1])

        def build(u: int, l: int, r: int):
            mn[u] = mx[u] = 0
            lazy[u] = 0
            if l == r:
                return
            m = (l + r) // 2
            build(u * 2, l, m)
            build(u * 2 + 1, m + 1, r)

        def range_add(u: int, l: int, r: int, ql: int, qr: int, v: int):
            if ql <= l and r <= qr:
                apply(u, v)
                return
            push(u)
            m = (l + r) // 2
            if ql <= m:
                range_add(u * 2, l, m, ql, qr, v)
            if qr > m:
                range_add(u * 2 + 1, m + 1, r, ql, qr, v)
            pull(u)

        # Find smallest index pos such that prefix_sum[pos] == target.
        # We can descend because if target is within [mn, mx] of a node, it exists inside that segment.
        def find_first(u: int, l: int, r: int, target: int) -> int:
            if l == r:
                return l
            push(u)
            m = (l + r) // 2
            left = u * 2
            if mn[left] <= target <= mx[left]:
                return find_first(left, l, m, target)
            return find_first(left + 1, m + 1, r, target)

        build(1, 0, n)

        last = {}          # value -> last position (1-indexed positions)
        now = 0            # current prefix sum at position i
        ans = 0

        # i is 1..n (right endpoint)
        for i, x in enumerate(nums, start=1):
            det = 1 if (x & 1) else -1

            # If x appeared before, remove its old contribution from [last[x]..n]
            if x in last:
                range_add(1, 0, n, last[x], n, -det)
                now -= det

            # Add current contribution at i to [i..n]
            last[x] = i
            range_add(1, 0, n, i, n, det)
            now += det

            # Earliest pos with prefix_sum[pos] == now gives max length ending at i
            pos = find_first(1, 0, n, now)
            ans = max(ans, i - pos)

        return ans
    