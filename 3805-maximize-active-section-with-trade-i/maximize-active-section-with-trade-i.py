class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        original_ones = s.count("1")
        groups = []

        i = 0
        while i < len(s):
            j = i

            while j < len(s) and s[j] == s[i]:
                j += 1

            groups.append((s[i], j - i))
            i = j

        best_gain = 0

        for i in range(1, len(groups) - 1):
            char, length = groups[i]

            if (
                char == "1"
                and groups[i - 1][0] == "0"
                and groups[i + 1][0] == "0"
            ):
                left_zeros = groups[i - 1][1]
                right_zeros = groups[i + 1][1]

                best_gain = max(
                    best_gain,
                    left_zeros + right_zeros
                )

        return original_ones + best_gain