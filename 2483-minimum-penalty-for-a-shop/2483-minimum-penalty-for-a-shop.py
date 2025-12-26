class Solution:
    def bestClosingTime(self, customers: str) -> int:
        n = len(customers)
        minPen = inf
        hourMinPen = 0

        prefixNArr = [0] * (n+1)
        suffixYArr = [0] * (n+1)

        for i,c in enumerate(customers):
            prefixNArr[i+1] = prefixNArr[i] + (1 if c == "N" else 0)
        
        for i in range(n-1, -1, -1):
            suffixYArr[i] = suffixYArr[i+1] + (1 if customers[i] == "Y" else 0)

        for j in range(n+1):
            curPen = prefixNArr[j] + suffixYArr[j]
            print(curPen)
            if curPen < minPen :
                minPen = curPen
                hourMinPen = j
        return hourMinPen
