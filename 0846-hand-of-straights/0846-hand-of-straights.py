import heapq
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0: return False #There is no way to split arr in groupSize groups.
        hashTable = {}
        for card in hand:
            hashTable[card] = hashTable.get(card , 0) + 1
        
        minHeap = []
        for card in set(hand):
            heapq.heappush(minHeap, card)

        curGroup = []
        while minHeap:
            curMin = minHeap[0]
            
            for i in range(curMin, curMin + groupSize):
                if i not in hashTable or hashTable[i] == 0:
                    return False
                hashTable[i] -= 1
                if hashTable[i] == 0: 
                    if i != minHeap[0]: return False
                    heapq.heappop(minHeap)
        return True


        print(hashTable, minHeap)

        


# [1, 2, 2, 3, 3, 4, 6, 7, 8]
# [2, 2, 3, 3, 4, 6, 7, 8]
# [2, 3, 3, 4, 6, 7, 8]


# 8, 10, 12 i = 0, pop 8
# 10, 12 i = 0
#

# [1, 1, 2, 2, 3, 3, 3, 4]
# [1, 2, 2, 3, 3, 3, 4]
# [1, 2, 3, 3, 3, 4]
# [3, 3, 3, 4]
# [3, 3]

