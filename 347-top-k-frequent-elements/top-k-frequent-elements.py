class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Step 1: Count frequencies
        topFreq = {}
        for num in nums:
            topFreq[num] = 1 + topFreq.get(num, 0)
        
        # Step 2: Group numbers by frequency
        ordered = defaultdict(list)
        for num, freq in topFreq.items():
            ordered[freq].append(num)

        # Step 3: Iterate from highest to lowest frequency
        res = []
        for freq in sorted(ordered.keys(), reverse=True):
            for num in ordered[freq]:
                if k > 0:
                    res.append(num)
                    k -= 1
                else:
                    return res

        return res
