MX = 10**6 + 10
sieve = [True] * MX
sieve[0], sieve[1] = False, False
spf = [0] * MX

for i in range(2, MX):
    if sieve[i]: 
        spf[i] = i
        for j in range(i + i, MX, i):
            sieve[j] = False
            if spf[j] == 0: spf[j] = i

def get_factors(x):
    res = set()
    while x > 1:
        p = spf[x]
        res.add(p)
        x //= p
    return res

class Solution:
    def minJumps(self, nums: List[int]) -> int:
        n = len(nums)
        groups = defaultdict(list)

        for i, x in enumerate(nums):
            for p in get_factors(x):
                groups[p].append(i)
        q = deque()
        q.append((0,0)) #i, jumps

        seen_i = set()
        seen_i.add(0)
        seen_p = set()

        while q :
            i, jumps = q.popleft()
            if i == n-1: return jumps

            if i + 1 < n and not i +1 in seen_i:
                q.append((i+1, jumps + 1))
                seen_i.add(i+1)
            
            if i -1 >= 0 and not i -1 in seen_i:
                q.append((i-1, jumps + 1))
                seen_i.add(i-1)

            if nums[i] in groups and not nums[i] in seen_p:
                seen_p.add(nums[i])
                for j in groups[nums[i]]:
                    if not j in seen_i:
                        q.append((j, jumps + 1))
                        seen_i.add(j)

