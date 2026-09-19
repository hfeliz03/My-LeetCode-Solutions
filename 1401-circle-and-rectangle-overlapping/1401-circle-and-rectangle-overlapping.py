class Solution:
    def checkOverlap(self, radius: int, xCenter: int, yCenter: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        if x2 < xCenter: closex = x2
        elif x1 > xCenter: closex = x1
        else: closex = xCenter

        if y2 < yCenter: closey = y2
        elif y1 > yCenter: closey = y1
        else: closey = yCenter

        return True if sqrt((xCenter - closex)**2 + (yCenter - closey)**2) <= radius else False