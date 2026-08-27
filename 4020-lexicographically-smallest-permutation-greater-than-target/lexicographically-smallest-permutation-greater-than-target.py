from collections import Counter

class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        ctr = Counter(s)
        n = len(s)

        def dfs(i, greater):
            if i == n:
                return "" if greater else None

            for c in sorted(ctr):
                if ctr[c] == 0:
                    continue

                # If we're still equal to target so far,
                # we cannot choose something smaller.
                if not greater and c < target[i]:
                    continue

                ctr[c] -= 1

                newGreater = greater or c > target[i]
                suffix = dfs(i + 1, newGreater)

                if suffix is not None:
                    return c + suffix

                ctr[c] += 1

            return None

        res = dfs(0, False)
        return res if res is not None else ""