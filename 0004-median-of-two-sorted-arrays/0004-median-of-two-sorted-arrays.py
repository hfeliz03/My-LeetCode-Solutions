class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)
        i, j, o = 0, 0, 0
        curr = []

        def shiftPointer(numArray):
            nonlocal i, j, o
            if numArray == 1:
                curr.append(nums1[i])
                i+=1
            else:
                curr.append(nums2[j])
                j+=1
            o += 1

        while i < m and j < n:
            if nums1[i] < nums2[j]:
                shiftPointer(1)
            else:
                shiftPointer(2)

            if o > (m+n)/2: 
                return (curr[-1] + curr[-2])/2 if (m+n) % 2 == 0 else curr[-1]

        while i < m and o <= (m+n)/2:
            shiftPointer(1)

        while j < n and o <= (m+n)/2:
            shiftPointer(2)

        return (curr[-1] + curr[-2])/2 if (m+n) % 2 == 0 else curr[-1]
        

