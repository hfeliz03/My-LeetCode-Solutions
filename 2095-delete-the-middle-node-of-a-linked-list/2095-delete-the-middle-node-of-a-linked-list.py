# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curSlow, curFast = head, head
        prevCurSlow = None
        while curFast and curFast.next :
            prevCurSlow = curSlow
            curSlow = curSlow.next
            curFast = curFast.next.next
        
        if prevCurSlow :
            prevCurSlow.next = prevCurSlow.next.next
        else: 
            head = None 
        return head