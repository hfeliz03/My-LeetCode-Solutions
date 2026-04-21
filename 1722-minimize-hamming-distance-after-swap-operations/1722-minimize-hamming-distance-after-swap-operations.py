class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        #This was genuinely hard to think of AND code 
        n = len(source)

        parent = list(range(n)) #0,1,2,....n 
        rank = [0] * n #[0,0,0,0,...0]

        def find(x: int) -> int:
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x: int, y: int) -> None:
            rx, ry = find(x), find(y)
            if rx == ry:
                return

            if rank[rx] < rank[ry]:
                parent[rx] = ry
            elif rank[rx] > rank[ry]:
                parent[ry] = rx
            else:
                parent[ry] = rx
                rank[rx] += 1

        # Build connected components
        for a, b in allowedSwaps:
            union(a, b)

        # Group indices by component root
        groups = defaultdict(list)
        for i in range(n):
            root = find(i)
            groups[root].append(i)

        # Count mismatches component by component
        answer = 0

        for indices in groups.values():
            source_count = Counter(source[i] for i in indices)
            target_count = Counter(target[i] for i in indices)

            # Anything extra in source that cannot be matched adds to answer
            for val, freq in source_count.items():
                matched = min(freq, target_count.get(val, 0))
                answer += freq - matched

        return answer
