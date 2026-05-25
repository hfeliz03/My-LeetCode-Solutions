class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        n = len(s)

        if s[-1] != "0": return False

        q = deque([0])
        farthest = 0

        while q:
            i = q.popleft()
            start = max(i + minJump, farthest + 1)
            end = min(i + maxJump, n - 1)

            for j in range(start, end + 1):
                if s[j] == "0":
                    if j == n - 1: return True

                    q.append(j)
            
            farthest = max(farthest, end)

        return False
