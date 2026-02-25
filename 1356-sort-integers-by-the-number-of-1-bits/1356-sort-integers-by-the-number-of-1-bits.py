class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        res = []
        resDict = {}
        for num in arr:
            binary = bin(num)[2:]
            num1s = sum([int(char) for char in  binary])
            atNum1s = resDict.get(num1s, [])
            atNum1s.append(binary)
            resDict[num1s] = atNum1s

        for setOfSame1s in sorted(resDict.keys()):
            currArr = resDict[setOfSame1s]
            for i in range(len(currArr)):
                currArr[i] = int(currArr[i],2)
            res.append(sorted(currArr))

        print(res)
        return [number for sublist in res for number in sublist]