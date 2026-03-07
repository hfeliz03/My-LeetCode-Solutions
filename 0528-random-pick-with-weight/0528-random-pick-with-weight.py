import random


class Solution:

    def __init__(self, w: List[int]):
        self.sumW = sum(w)
        self.sumProb = 0
        self.probs = []
        for num in w:    #[1,3]
            self.sumProb = self.sumProb+(num/self.sumW)
            self.probs.append(self.sumProb) #[0.25,1]

    def pickIndex(self) -> int:
        randomizedIVal = random.random()
        l, r = 0, len(self.probs)-1
        while l <= r:
            mid = ((r-l) // 2) + l
            if randomizedIVal <= self.probs[mid]:
                r = mid - 1
            else:
                l = mid + 1

        return l

#.12 .56 .04 .28
#0.12, 0.68, 0.7200000000000001, 1.0
# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()