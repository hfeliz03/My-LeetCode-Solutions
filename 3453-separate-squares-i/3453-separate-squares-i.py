# class Solution:
#     def separateSquares(self, squares: List[List[int]]) -> float:
#         #The area of each square is just l*l
#         #We can find the y value at the toop of each square by simply getting yi and adding to it li
#         areaAndTopYi = []

#         for square in squares:
#             areaAndTopYi.append([square[2]**2, square[1]+square[2]] )
        
#         sumBelow, sumAbove = 0, sum(areaAndTopYi[0])

#         separateSquares = float("inf")
#         for area, topY in areaAndTopYi :
#             sumBelow += area
#             sumAbove -= area
#             if sumBelow == sumAbove :
#                 separateSquares = min(separateSquares, topY)
#                 break

from typing import List

class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        # Overlaps counted multiple times => total area is sum of l^2
        total = 0.0
        events = []  # (y, deltaSlope) where slope is d(A_below)/dy

        for x, y, l in squares:
            total += l * l
            # entering the square: slope increases by l
            events.append((y, +l))
            # leaving the square: slope decreases by l
            events.append((y + l, -l))

        target = total / 2.0
        events.sort()

        # If total area is 0 (degenerate), any y works; return 0.0
        if total == 0:
            return 0.0

        # Sweep between consecutive distinct y's
        i = 0
        prev_y = events[0][0]
        slope = 0.0      # current derivative of A_below wrt y
        below = 0.0      # A_below(prev_y)

        # Apply all events at the starting y so slope is correct just above prev_y
        while i < len(events) and events[i][0] == prev_y:
            slope += events[i][1]
            i += 1

        # Before the first event, below=0 < target (since total>0), so answer >= prev_y
        while i < len(events):
            y = events[i][0]
            dy = y - prev_y

            if dy > 0:
                # On (prev_y, y), below increases linearly: below(y') = below + slope*(y'-prev_y)
                if slope == 0.0:
                    # below stays constant across this interval
                    if abs(below - target) <= 1e-12:
                        return float(prev_y)  # minimal y achieving equality
                else:
                    end_below = below + slope * dy
                    # Check if target is hit within this interval
                    if (below <= target <= end_below) or (below >= target >= end_below):
                        return float(prev_y + (target - below) / slope)
                    below = end_below

            # Move to y, then apply all events at y (tops/bottoms)
            prev_y = y
            while i < len(events) and events[i][0] == y:
                slope += events[i][1]
                i += 1

            # If we hit target exactly at an event y, that's the minimal such y
            if abs(below - target) <= 1e-12:
                return float(prev_y)

        # Shouldn't happen (below ends at total), but as a fallback:
        return float(prev_y)

#         return separateSquares

