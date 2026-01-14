from typing import List
from bisect import bisect_left

class SegmentTree:
    def __init__(self, xs: List[int]):
        self.xs = xs
        self.n = len(xs) - 1  # number of elementary segments [xs[i], xs[i+1])
        self.count = [0] * (4 * self.n)
        self.covered = [0] * (4 * self.n)

    def _pull(self, pos: int, l: int, r: int) -> None:
        if self.count[pos] > 0:
            self.covered[pos] = self.xs[r + 1] - self.xs[l]
        elif l == r:
            self.covered[pos] = 0
        else:
            self.covered[pos] = self.covered[pos * 2 + 1] + self.covered[pos * 2 + 2]

    def update(self, ql: int, qr: int, val: int, pos: int = 0, l: int = 0, r: int = None) -> None:
        if r is None:
            r = self.n - 1
        if ql > r or qr < l:
            return  # no overlap
        if ql <= l and r <= qr:
            self.count[pos] += val
            self._pull(pos, l, r)
            return

        mid = (l + r) // 2
        self.update(ql, qr, val, pos * 2 + 1, l, mid)
        self.update(ql, qr, val, pos * 2 + 2, mid + 1, r)
        self._pull(pos, l, r)

    def query(self) -> int:
        return self.covered[0] if self.n > 0 else 0


class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        xs = set()
        events = []  # (y, x1, x2, +1/-1)

        for x, y, size in squares:
            x1, x2 = x, x + size
            xs.add(x1)
            xs.add(x2)
            events.append((y, x1, x2, +1))
            events.append((y + size, x1, x2, -1))

        xs = sorted(xs)
        events.sort()

        st = SegmentTree(xs)

        def x_to_seg_index(a: int, b: int):
            i = bisect_left(xs, a)
            j = bisect_left(xs, b) - 1  # inclusive segment index
            return i, j

        # 1) total union area
        total_area = 0.0
        prev_y = events[0][0]

        for y, x1, x2, op in events:
            total_area += st.query() * (y - prev_y)
            i, j = x_to_seg_index(x1, x2)
            if i <= j:  # interval has positive width
                st.update(i, j, op)
            prev_y = y

        # 2) find smallest y where prefix area reaches half
        target = total_area / 2.0
        st = SegmentTree(xs)  # reset
        acc = 0.0
        prev_y = events[0][0]

        for y, x1, x2, op in events:
            width = st.query()
            dy = y - prev_y
            if dy > 0 and width > 0:
                band = width * dy
                if acc + band >= target:
                    return prev_y + (target - acc) / width
                acc += band

            i, j = x_to_seg_index(x1, x2)
            if i <= j:
                st.update(i, j, op)
            prev_y = y

        return float(prev_y)