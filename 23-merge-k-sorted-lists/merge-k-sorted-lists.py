# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        newList = ListNode()
        dummy = newList
        pointers = [head for head in lists]

        while any(pointers):
            
            i, currSmallest = 0, None
            currSmallestIndex = -1 
            while i < len(pointers):
                if pointers[i] and ( not currSmallest or pointers[i].val < currSmallest.val):
                    currSmallest = pointers[i]
                    currSmallestIndex = i
                i+=1
            dummy.next = currSmallest
            dummy = dummy.next
            pointers[currSmallestIndex] = pointers[currSmallestIndex].next
        
        return newList.next
        
        