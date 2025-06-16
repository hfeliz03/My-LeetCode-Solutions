# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr, prev = head, head
        numElements = 0
        while curr:
            numElements +=1
            curr = curr.next
        
        indexToRemove = numElements - n
        if indexToRemove == 0: return head.next
        curr = head
        while indexToRemove >= 1:
            prev = curr
            curr = curr.next
            indexToRemove -= 1
        prev.next = curr.next
        return head