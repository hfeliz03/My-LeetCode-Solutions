class Solution:
    #I bruteforced this somehow
    # def maxSumTrionic(self, nums: List[int]) -> int:
    #     n = len(nums)
    #     maxSum = -10**9
    #     def isTrionic(nums: List[int]) -> bool:
    #         p, q = -1, -1
    #         for i in range(1, len(nums)):
    #             if (nums[i] < nums[i-1]) and (p == -1 )and (i-1 != 0):
    #                 p = i-1
    #             elif nums[i] > nums[i-1] and p != -1 and q == -1:
    #                 q = i
    #             elif nums[i] > nums[i-1] and ((p == -1 and q == -1) or (p != -1 and q != -1)):
    #                 continue
    #             elif nums[i] < nums[i-1] and p != -1 and q == -1:
    #                 continue
    #             else:
    #                 return False
    #         return p != -1 and q != -1

    #     i = 0 
    #     j = i + 3
    #     while i < n-2:
    #         if nums[i] <= 0:
    #             i+= 1
    #             j+= 1
    #         while j <= n:
    #             if isTrionic(nums[i:j]) :
    #                 maxSum = max(sum(nums[i:j]), maxSum)
    #             j+=1
    #         i += 1
    #         j = i + 3
        
    #     return maxSum
    #Not my answer
    def maxSumTrionic(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 4:
            return -10**18  # or whatever the problem expects when impossible

        NEG = -10**18

        up = NEG    # phase 1: increasing, length >= 2, ending at i
        down = NEG  # phase 2: decreasing, length >= 2, ending at i
        up2 = NEG   # phase 3: increasing, length >= 2, ending at i

        ans = NEG

        for i in range(1, n):
            new_up = NEG
            new_down = NEG
            new_up2 = NEG

            # Phase 1 (increasing)
            if nums[i - 1] < nums[i]:
                # start a new increasing run of length 2: nums[i-1], nums[i]
                new_up = max(new_up, nums[i - 1] + nums[i])
                # extend existing phase-1 run
                if up != NEG:
                    new_up = max(new_up, up + nums[i])

                # Phase 3 (increasing again)
                # start phase 3 after a valid phase 2
                if down != NEG:
                    new_up2 = max(new_up2, down + nums[i])
                # extend existing phase 3
                if up2 != NEG:
                    new_up2 = max(new_up2, up2 + nums[i])

            # Phase 2 (decreasing)
            if nums[i - 1] > nums[i]:
                # start phase 2 after a valid phase 1
                if up != NEG:
                    new_down = max(new_down, up + nums[i])
                # extend existing phase 2
                if down != NEG:
                    new_down = max(new_down, down + nums[i])

            up, down, up2 = new_up, new_down, new_up2
            ans = max(ans, up2)

        return ans