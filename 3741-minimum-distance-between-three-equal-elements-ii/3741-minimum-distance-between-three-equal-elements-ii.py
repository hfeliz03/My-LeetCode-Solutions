class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        minDistance = 10**6
        myDict = defaultdict(list)
        for i, num in enumerate(nums):
            myDict[num].append(i)
        
        for k in list(myDict.keys()):
            if len(myDict[k]) < 3 : del myDict[k]
        
        if not myDict: return -1

        #Get minDistance
        for k, v in myDict.items():
            for i in range(0, len(v)-2):
                curDistance = abs(v[i] - v[i+1]) + abs(v[i] - v[i+2]) + abs(v[i+2] - v[i+1])
                minDistance = min(minDistance, curDistance)

        return minDistance 