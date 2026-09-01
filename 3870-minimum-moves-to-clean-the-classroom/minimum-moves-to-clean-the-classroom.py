#Did not solve this one
from collections import deque
from typing import List

class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:
        rows, cols = len(classroom), len(classroom[0])

        litter_id = {}
        start = None

        for r in range(rows):
            for c in range(cols):
                if classroom[r][c] == "S":
                    start = (r, c)
                elif classroom[r][c] == "L":
                    litter_id[(r, c)] = len(litter_id)

        target_mask = (1 << len(litter_id)) - 1

        if target_mask == 0:
            return 0

        # r, c, collected_mask, remaining_energy
        queue = deque([(start[0], start[1], 0, energy)])
        moves = 0

        # For a given position and collected mask, keep the greatest
        # remaining energy reached so far.
        best_energy = {
            (start[0], start[1], 0): energy
        }

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while queue:
            for _ in range(len(queue)):
                r, c, mask, remaining = queue.popleft()

                # Cannot leave a non-reset cell with zero energy
                if remaining == 0:
                    continue

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc

                    if not (0 <= nr < rows and 0 <= nc < cols):
                        continue

                    if classroom[nr][nc] == "X":
                        continue

                    new_energy = remaining - 1
                    new_mask = mask

                    if classroom[nr][nc] == "R":
                        new_energy = energy

                    if classroom[nr][nc] == "L":
                        litter_index = litter_id[(nr, nc)]
                        new_mask |= 1 << litter_index

                    if new_mask == target_mask:
                        return moves + 1

                    state = (nr, nc, new_mask)

                    # More energy at the same position with the same litter
                    # collected dominates a state with less energy.
                    if best_energy.get(state, -1) >= new_energy:
                        continue

                    best_energy[state] = new_energy
                    queue.append((nr, nc, new_mask, new_energy))

            moves += 1

        return -1