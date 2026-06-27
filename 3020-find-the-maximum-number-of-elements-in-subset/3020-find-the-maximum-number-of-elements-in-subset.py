# from collections import Counter
# class Solution:
#     def maximumLength(self, nums: List[int]) -> int:
#         ctr = Counter(nums)
#         nums = sorted(list(set(nums)))
#         res = 1
#         for num in nums:
#             curRes = 2
#             if ctr[num] >= 2:
#                 curNum = num
#                 while True:
#                     if curNum**2 in ctr:
#                         curRes += 1
#                         res = max(res, curRes)
#                         curNum = curNum**2
#                     else:
#                         #curRes += 1
#                         res = max(res, curRes)
#                         break
        # return res

from collections import Counter

from typing import List

class Solution:

    def maximumLength(self, nums: List[int]) -> int:

        ctr = Counter(nums)

        res = 1

        for num in ctr:

            # Special case: 1 -> 1,1,1,1...

            if num == 1:

                if ctr[1] % 2 == 1:

                    res = max(res, ctr[1])

                else:

                    res = max(res, ctr[1] - 1)
                continue
            cur = num
            length = 0
            while cur in ctr:
                if ctr[cur] >= 2:
                    length += 2
                    cur = cur * cur
                else:
                    length += 1
                    break

            # If we ended because next square doesn't exist,
            # the last paired number cannot actually be used twice.

            if cur not in ctr:
                length -= 1
            res = max(res, length)

        return res