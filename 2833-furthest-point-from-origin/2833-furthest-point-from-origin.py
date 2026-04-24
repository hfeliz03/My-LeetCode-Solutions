from collections import Counter
class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        ctr = Counter(moves)
        return (max(ctr["L"], ctr["R"]) + ctr["_"]) - min(ctr["L"], ctr["R"])