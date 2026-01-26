class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        minAbsDif = 10**5
        pairs = []

        for i in range(len(arr)-1):
            a, b = arr[i], arr[i+1] 
            if abs(b-a) < minAbsDif:
                minAbsDif = abs(b-a)
                pairs = [[a,b]]
            elif abs(b-a) == minAbsDif:
                pairs.append([a,b])
            else:
                continue
        
        return pairs