class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)
        n = len(nums2)
        o = 0
        i,j = 0, 0
        curr = []
        while i < m and j < n:
            if nums1[i] < nums2[j]:
                curr.append(nums1[i])
                i+=1
            else:
                curr.append(nums2[j])
                j+=1
            o+=1 
            # print(curr)
            # print(o)
            if o > (m+n)/2: 
                return (curr[-1] + curr[-2])/2 if (m+n) % 2 == 0 else curr[-1]

        while i < m and o <= (m+n)/2:
            curr.append(nums1[i])
            i+=1
            o+=1 

        while j < n and o <= (m+n)/2:
            curr.append(nums2[j])
            j+=1
            o+=1 
            print(curr)
            print(o)

        return (curr[-1] + curr[-2])/2 if (m+n) % 2 == 0 else curr[-1]
        

