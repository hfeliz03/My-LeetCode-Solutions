import random


class Solution:

    def __init__(self, w: List[int]):
        self.w = w
        self.sumW = sum(w)
        self.sumProb = 0
        self.probs = []
        for i, num in enumerate(self.w):    #[1,3]
            self.sumProb = self.sumProb+(num/self.sumW)
            self.probs.append(self.sumProb) #[0.25,1]

    def pickIndex(self) -> int:
        randomizedIVal = random.random()
        res = 0
        for i in range(len(self.probs)-1, -1, -1):
            if randomizedIVal > self.probs[i]: 
                res = i+1
                break
        return res

#.12 .56 .04 .28
# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()