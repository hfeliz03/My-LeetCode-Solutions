class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        minAbsDif = 10**5
        pairs = []

        for i in range(len(arr)-1):
            a, b = arr[i], arr[i+1] 
            dif = abs(b-a)
            if dif < minAbsDif:
                minAbsDif = dif
                pairs = [[a,b]]
            elif dif == minAbsDif:
                pairs.append([a,b])
            else:
                continue
        
        return pairs