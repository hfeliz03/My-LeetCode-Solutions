import heapq
class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        n = len(nums)
        if (n<=1): return 0

        #Build doubly LinkedList (O(n))
        prevLL, nextLL = [], []

        for i in range(n):
            prevLL.append(i-1)
            nextLL.append(i+1) if i < len(nums)-1 else nextLL.append(-1)

        #Build array of all the to be removed elements
        removed = [0] * n

        #number of iolations: i1 > i2
        violations = 0

        #Min Heap: (sum, 1st Index)
        min_heap = []
        for i in range(n-1):
            heapq.heappush(min_heap, (nums[i]+nums[i+1], i) )
            if nums[i] > nums[i+1]: violations+=1

        if violations == 0: return 0 #Already in nondecreasing order

        operations = 0

        while violations > 0:
            curSum, u = heapq.heappop(min_heap)
            
            if(removed[u]): continue
            v = nextLL[u]
            if(v == -1 or removed[v]) : continue
            if(nums[u] + nums[v] != curSum): continue

            p = prevLL[u]
            nv = nextLL[v]

            #Remove old violations
            if (p != -1 and nums[p] > nums[u]): violations -= 1
            if(nums[u] > nums[v]): violations -= 1
            if (nv != -1 and nums[v] > nums[nv]): violations -= 1

            #Merge u and v
            nums[u] += nums[v]
            removed[v] = 1
            nextLL[u] = nv
            if(nv!=-1) : prevLL[nv] = u

            #Count new violations (if any)
            if (p != -1 and nums[p] > nums[u]): violations +=1 
            if (nv != -1 and nums[u] > nums[nv]): violations +=1 

            #Push new candidate pairs
            if (p != -1): heapq.heappush(min_heap, (nums[p] + nums[u], p))
            if (nv != -1): heapq.heappush(min_heap, (nums[u] + nums[nv], u))

            operations += 1 

        return operations
        
