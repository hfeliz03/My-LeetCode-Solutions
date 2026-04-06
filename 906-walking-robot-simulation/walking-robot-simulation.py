class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        obstacleSet = set(map(tuple, obstacles))

        # up, right, down, left
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        direction = 0  # start facing up

        x, y = 0, 0
        maxEuclid = 0

        for command in commands:
            if command == -1:   # turn right
                direction = (direction + 1) % 4
            elif command == -2: # turn left
                direction = (direction - 1) % 4
            else:
                dx, dy = directions[direction]

                for _ in range(command):
                    nx, ny = x + dx, y + dy

                    if (nx, ny) in obstacleSet:
                        break

                    x, y = nx, ny
                    maxEuclid = max(maxEuclid, x * x + y * y)

        return maxEuclid