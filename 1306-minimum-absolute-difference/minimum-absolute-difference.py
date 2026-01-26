class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        minAbsDif = 10**5
        pairs = []

        for i in range(len(arr)-1):
            dif = arr[i+1] - arr[i]
            if dif < minAbsDif:
                minAbsDif = dif
                pairs = [[arr[i],arr[i+1]]]
            elif dif == minAbsDif:
                pairs.append([arr[i],arr[i+1]])
        
        return pairs