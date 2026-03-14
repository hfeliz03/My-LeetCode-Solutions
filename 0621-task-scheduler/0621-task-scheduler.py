from collections import Counter
import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freqs = Counter(tasks)
        maxFreq = max(freqs.values())
        countMax = sum(1 for f in freqs.values() if f == maxFreq)

        return max(len(tasks), (maxFreq - 1) * (n + 1) + countMax)