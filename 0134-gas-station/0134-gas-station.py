class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total = tank = start = 0

        for i in range(len(gas)):
            diff = gas[i] - cost[i]
            total += diff
            tank += diff
            if tank < 0:
                start = i + 1
                tank = 0
        
        return start if total >= 0 else -1
    
        # diffs = []
        # for i in range(len(gas)): diffs.append(gas[i] - cost[i])
            
        # print(diffs)
        # if sum(diffs) < 0 : return -1
        # #Check if possible to do the entire loop
        # tankSums = []
        # bestI = 0
        # bestSum = 0
        # for i in range(len(diffs)):
        #     if diffs[i] <= 0: continue # we dont want to start at a negative difference
        #     curI = (i +  1) % len(diffs)
        #     curSum = diffs[i]
        #     while curI != i:
        #         if curSum + diffs[curI] >= 0:
        #             curSum += diffs[curI]
        #         else: break

        #         if bestSum <= curSum :
        #             bestSum = curSum 
        #             bestI = i
        #         curI = (curI + 1) % len(diffs)

        # return bestI



        # maxDiff = -10**5
        # maxDiffI = -1
        # for i in range(len(gas)):
        #     if gas[i] - cost[i] > maxDiff:
        #         maxDiff = gas[i] - cost[i]
        #         maxDiffI = i
            
        # print(maxDiffI)
        # #Check if possible to do the entire loop
        # currI = (maxDiffI +  1) % len(gas)
        # currTank = gas[maxDiffI] - cost[maxDiffI]
        # while currI != maxDiffI:
        #     currTank += gas[currI] - cost[currI]
        #     currI = (currI + 1) % len(gas)

        # return maxDiffI if currTank >=0 else -1