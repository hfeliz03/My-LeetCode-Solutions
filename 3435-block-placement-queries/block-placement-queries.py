####I DID NOT SOLVE THIS
class Solution:
    def getResults(self, queries: List[List[int]]) -> List[bool]:
        M = max(q[1] for q in queries) + 2

        # Fenwick tree for obstacle positions
        bit = [0] * (M + 1)

        def add(i, v):
            i += 1
            while i <= M:
                bit[i] += v
                i += i & -i

        def pref(i):
            i += 1
            s = 0
            while i > 0:
                s += bit[i]
                i -= i & -i
            return s

        def kth(k):  # smallest index with prefix >= k
            idx = 0
            step = 1 << (M.bit_length())
            while step:
                ni = idx + step
                if ni <= M and bit[ni] < k:
                    idx = ni
                    k -= bit[ni]
                step //= 2
            return idx

        # Segment tree for max gap ending at each obstacle
        size = 1
        while size < M + 1:
            size *= 2
        seg = [0] * (2 * size)

        def update(i, val):
            i += size
            seg[i] = val
            i //= 2
            while i:
                seg[i] = max(seg[2*i], seg[2*i+1])
                i //= 2

        def query(l, r):
            l += size
            r += size
            ans = 0
            while l <= r:
                if l % 2 == 1:
                    ans = max(ans, seg[l])
                    l += 1
                if r % 2 == 0:
                    ans = max(ans, seg[r])
                    r -= 1
                l //= 2
                r //= 2
            return ans

        # Sentinel obstacles at 0 and M
        add(0, 1)
        add(M, 1)
        update(0, 0)
        update(M, M)

        ans = []

        for q in queries:
            if q[0] == 1:
                x = q[1]

                c = pref(x)
                prev_obs = kth(c)
                next_obs = kth(c + 1)

                add(x, 1)

                update(x, x - prev_obs)
                update(next_obs, next_obs - x)

            else:
                _, x, sz = q

                c = pref(x)
                prev_obs = kth(c)

                best_full_gap = query(0, prev_obs)
                tail_gap = x - prev_obs

                ans.append(max(best_full_gap, tail_gap) >= sz)

        return ans