class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        n = len(moves)
        #LLRLLLR 5-2 = 3
        #LRRLRRR 5-2 = 3
        numUnds = 0
        numLs, numRs = 0 , 0
        for i in moves:
            if i == "_": numUnds+=1
            elif i == "L": numLs+= 1
            else: numRs+=1
        return (max(numLs, numRs) + numUnds) - min(numLs, numRs)