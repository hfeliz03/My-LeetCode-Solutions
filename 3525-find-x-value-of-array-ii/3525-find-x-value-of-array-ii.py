from typing import List

class Solution:
    def resultArray(
        self,
        nums: List[int],
        k: int,
        queries: List[List[int]]
    ) -> List[int]:

        n = len(nums)

        # Each node = (product % k, prefix_counts)
        # prefix_counts[r] = number of prefixes with product % k == r
        tree = [None] * (4 * n)

        def merge(left, right):
            left_prod, left_cnt = left
            right_prod, right_cnt = right

            prod = (left_prod * right_prod) % k
            cnt = left_cnt[:]

            # Prefixes that extend from the left segment
            # into the right segment
            for r in range(k):
                new_r = (left_prod * r) % k
                cnt[new_r] += right_cnt[r]

            return (prod, cnt)

        def build(node, l, r):
            if l == r:
                val = nums[l] % k

                cnt = [0] * k
                cnt[val] = 1

                tree[node] = (val, cnt)
                return

            mid = (l + r) // 2

            build(node * 2, l, mid)
            build(node * 2 + 1, mid + 1, r)

            tree[node] = merge(
                tree[node * 2],
                tree[node * 2 + 1]
            )

        def update(node, l, r, idx, val):
            if l == r:
                val %= k

                cnt = [0] * k
                cnt[val] = 1

                tree[node] = (val, cnt)
                return

            mid = (l + r) // 2

            if idx <= mid:
                update(node * 2, l, mid, idx, val)
            else:
                update(node * 2 + 1, mid + 1, r, idx, val)

            tree[node] = merge(
                tree[node * 2],
                tree[node * 2 + 1]
            )

        def query(node, l, r, ql, qr):
            if ql <= l and r <= qr:
                return tree[node]

            mid = (l + r) // 2

            if qr <= mid:
                return query(node * 2, l, mid, ql, qr)

            if ql > mid:
                return query(node * 2 + 1, mid + 1, r, ql, qr)

            left = query(node * 2, l, mid, ql, qr)
            right = query(node * 2 + 1, mid + 1, r, ql, qr)

            return merge(left, right)

        build(1, 0, n - 1)

        ans = []

        for index, value, start, x in queries:

            # Apply the update
            update(1, 0, n - 1, index, value)

            # Look at nums[start:]
            prod, cnt = query(
                1, 0, n - 1,
                start, n - 1
            )

            ans.append(cnt[x])

        return ans