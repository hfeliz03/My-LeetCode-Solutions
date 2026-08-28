class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        n = len(s)
        cnt = Counter(s)

        # A palindrome can have at most one odd-frequency character.
        odd = [c for c in cnt if cnt[c] % 2 == 1]
        if len(odd) > 1:
            return ""

        middle = odd[0] if odd else ""

        # Characters available for the LEFT half.
        half = [0] * 26
        for c, freq in cnt.items():
            half[ord(c) - ord('a')] = freq // 2

        m = n // 2
        prefix = []

        def can_finish():
            """
            Build the lexicographically LARGEST possible palindrome
            given the current prefix.

            If even this isn't > target, no completion can work.
            """
            remaining = []

            # Largest remaining left half => descending order
            for i in range(25, -1, -1):
                remaining.extend(
                    [chr(ord('a') + i)] * half[i]
                )

            left = "".join(prefix + remaining)

            palindrome = left + middle + left[::-1]

            return palindrome > target

        # Greedily construct the smallest possible left half.
        for _ in range(m):
            chosen = False

            for i in range(26):
                if half[i] == 0:
                    continue

                # Try this character
                half[i] -= 1
                prefix.append(chr(ord('a') + i))

                if can_finish():
                    chosen = True
                    break

                # Undo
                prefix.pop()
                half[i] += 1

            if not chosen:
                return ""

        left = "".join(prefix)
        ans = left + middle + left[::-1]

        return ans if ans > target else ""