class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        maxDis = 0
        n, m = len(nums1), len(nums2)
        for i in range(n):
            j = maxDis + i
            while j < m:
                if nums1[i] > nums2[j]:
                    break
                else: #nums1[i] <= nums2[j]
                    maxDis = max(maxDis, j - i)
                j+=1
                
        return maxDis