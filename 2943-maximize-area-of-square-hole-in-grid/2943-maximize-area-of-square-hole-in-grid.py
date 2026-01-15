class Solution:
    def maximizeSquareHoleArea(self, n: int, m: int, hBars: List[int], vBars: List[int]) -> int:
        hBars.sort()
        vBars.sort()

        def best_run_len(bars: List[int]) -> int:
            if not bars: return 0

            cur = [bars[0], bars[0]]      # [start, end]
            best = [bars[0], bars[0]]     # best run [start, end]

            for i in range(1, len(bars)):
                if bars[i] == bars[i-1]: continue

                if bars[i] == bars[i-1] + 1:   # <-- consecutive
                    cur[1] = bars[i]
                else:
                    cur = [bars[i], bars[i]]

                # update best
                if (cur[1] - cur[0]) > (best[1] - best[0]):
                    best = [cur[0], cur[1]]

            # length of run = end-start+1
            return best[1] - best[0] + 1

        bestH = best_run_len(hBars)   # k horizontal bars in longest consecutive streak
        bestV = best_run_len(vBars)   # k vertical bars in longest consecutive streak

        side = min(bestH, bestV) + 1  # remove k bars => merge k+1 cells
        return side * side