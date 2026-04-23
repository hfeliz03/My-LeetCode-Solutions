class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        #Lowkey crazy math involved 
        res = [0] * len(nums)
        ctr, psum = defaultdict(list), defaultdict()
        for i, num in enumerate(nums):
            ctr[num].append(i)
        
        for key in ctr.keys():
            prefixSum = []
            for val in ctr[key]:
                prefixSum.append(prefixSum[-1] + val if prefixSum else val)
            psum[key] = (prefixSum)
        

        for key, indexArr in ctr.items():
            psumArr = psum[key]
            m = len(indexArr)

            for i, idx in enumerate(indexArr):
                left = idx * i - (psumArr[i - 1] if i > 0 else 0)
                right = (psumArr[-1] - psumArr[i]) - idx * (m - i - 1)
                res[idx] = left + right
        return res
