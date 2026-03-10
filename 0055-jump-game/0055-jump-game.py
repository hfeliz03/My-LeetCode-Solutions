class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # At each position reachable, check how far can we get by stoping at it.
        #We want to reach index n = 4
        #2, 4, 3, 4, 4 Therefore start at 0, check whats at 0 + 2, grab the one that takes you the farthest, and do that greedly.
        #If you cant progress because youve fell in a 0, at that index's reach add a negative value so reaching that point is not encouraged.
        if len(nums) <= 1: return True
        reach = []
        for i,num in enumerate(nums):
            reach.append(i+num)
        print(reach)
        i = 0
        bestI = 0
        l = i
        while i < len(nums):
            
            if reach[l] < i: #If we can no longer read the next index, just go to the one that was the best before
                l = bestI 
            
            if reach[i] >= reach[bestI] and reach[i] != 0:
                bestI = i

            if reach[bestI] >= len(nums)-1: return True
            
            if reach[bestI]> i:
                i+=1
            else: break
        
        return False