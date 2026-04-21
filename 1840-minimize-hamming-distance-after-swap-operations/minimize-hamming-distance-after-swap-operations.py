class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        n = len(source)
        parent = list(range(n))

        def find(x: int) -> int:
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(a: int, b: int) -> None:
            ra, rb = find(a), find(b)
            if ra != rb:
                parent[rb] = ra

        for a, b in allowedSwaps:
            union(a, b)

        groups = defaultdict(Counter)

        for i in range(n):
            root = find(i)
            groups[root][source[i]] += 1
            groups[root][target[i]] -= 1

        ans = 0
        for counter in groups.values():
            for v in counter.values():
                if v > 0:
                    ans += v

        return ans
