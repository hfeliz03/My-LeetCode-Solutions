class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        sumDivisors = 0
        numsWith4Divisors = {}
        for num in nums:
            r = int(math.isqrt(num))
            
            if not numsWith4Divisors.get(num):
                curDivisors = set([1,num])
            else:
                sumDivisors += numsWith4Divisors.get(num)
                continue
            
            i = 2

            while i <= r:
                if num % i == 0:
                    curDivisors.add(i)
                    curDivisors.add(num // i)
                if len(curDivisors) > 4: break
                i+=1
            
            if len(curDivisors) == 4:
                numsWith4Divisors[num] = sum(curDivisors)
                sumDivisors += numsWith4Divisors.get(num)
        
        return sumDivisors