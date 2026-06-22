from collections import defaultdict
class DetectSquares:
    #Each point is of the form (x,y): #
    #I want to have a max x, and a max y so i know how far I can expand
    def __init__(self):
        self.plane = defaultdict(int)
        self.setX = set()
        self.setY = set()


    def add(self, point: List[int]) -> None:
        x, y = point
        self.setX.add(x)
        self.setY.add(y)
        self.plane[(x, y)] += 1

    def count(self, point: List[int]) -> int:
        cnt = 0
        X, Y = point
        for x in self.setX:
            if x == X: continue

            side = abs(X - x)

            for newY in [Y + side, Y - side]:
                cnt += (
                    self.plane[(x, Y)] *
                    self.plane[(X, newY)] *
                    self.plane[(x, newY)]
                )
        return cnt

        


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)