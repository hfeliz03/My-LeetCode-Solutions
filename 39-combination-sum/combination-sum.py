class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        combi = []

        def helper(i, toAddArr, total):
            if total > target or i >= len(candidates): return
            if total == target: 
                combi.append(toAddArr.copy())
                return
                
            toAddArr.append(candidates[i])
            helper(i, toAddArr, total+candidates[i])
            toAddArr.pop()
            helper(i+1, toAddArr, total)

        helper(0, [], 0)
        return combi 