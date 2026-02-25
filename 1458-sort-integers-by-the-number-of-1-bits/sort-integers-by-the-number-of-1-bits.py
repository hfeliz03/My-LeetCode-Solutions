class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        res = []
        resDict = {}
        arr.sort()
        for num in arr:
            num1s = num.bit_count()
            atNum1s = resDict.get(num1s, [])
            atNum1s.append(num)
            resDict[num1s] = atNum1s #We know they got the same 

        for setOfSame1s in sorted(resDict.keys()):
            currArr = resDict[setOfSame1s] #Current array of the numbers with same number of 1
            res.append(currArr)

        print(res)
        return [number for sublist in res for number in sublist]