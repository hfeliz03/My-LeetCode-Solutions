class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        n = len(candidates)

        stack = []
        visitedSets = set()

        for i in range(n):
            if candidates[i] > target:
                continue
            stack.append(((candidates[i],), i, candidates[i]))

        while stack:
            curTup, lastIdx, curSum = stack.pop()

            if curSum == target:
                if curTup not in visitedSets:
                    res.append(list(curTup))
                    visitedSets.add(curTup)
                continue

            for j in range(lastIdx + 1, n):
                # skip duplicates at the same decision level
                if j > lastIdx + 1 and candidates[j] == candidates[j - 1]:
                    continue
                newSum = curSum + candidates[j]
                if newSum > target:
                    break
                stack.append((curTup + (candidates[j],), j, newSum))
        return res