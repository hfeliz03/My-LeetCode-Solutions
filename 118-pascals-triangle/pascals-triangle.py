class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows <= 0 :return []
        pascal = [[1]]
        for i in range(1, numRows):
            prev = pascal[-1]
            entry = []
            for j in range(0, len(prev)):
                if j == 0 : entry.append(prev[j])
                else: entry.append(prev[j - 1] + prev[j])
            entry.append(1)
            pascal.append(entry)
        return pascal