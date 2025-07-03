class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        if not temperatures : return [] 
        res = [0]*len(temperatures)
        stack = [0]
        for temp in range(1,len(temperatures)): 
            while stack and temperatures[temp] > temperatures[stack[-1]]:
                res[stack[-1]] = temp-stack[-1] 
                stack.pop()
            stack.append(temp)

        return res