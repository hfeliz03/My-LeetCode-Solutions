class Robot:

    def __init__(self, width: int, height: int):
        self.perimeter = 2*(height + width) - 4
        self.h, self.w = height, width
        self.pos = [0,0] #[x, y]
        self.dirs = [(1,0), (0,1), (-1,0), (0,-1)]
        self.di = 0

    def step(self, num: int) -> None:
        if num == 0: return 
        num %= self.perimeter
        if num == 0: num = self.perimeter
        
        for i in range(num):
            nx, ny = self.pos[0] + self.dirs[self.di][0], self.pos[1] + self.dirs[self.di][1]
            if nx < 0 or nx >= self.w or ny < 0 or ny >= self.h:
                self.di = (self.di + 1) % 4
                nx, ny = self.pos[0] + self.dirs[self.di][0], self.pos[1] + self.dirs[self.di][1]
            self.pos = [nx, ny]

    def getPos(self) -> List[int]:
        return self.pos

    def getDir(self) -> str:
        dire = ""
        if self.di == 0: dire = "East"
        elif self.di == 1: dire = "North"
        elif self.di == 2: dire = "West"
        else: dire = "South"
        return dire


# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.step(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()