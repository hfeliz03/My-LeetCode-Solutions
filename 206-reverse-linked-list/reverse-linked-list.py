# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        revHead = None
        curr = head
        while curr:
            temp = curr.next
            curr.next = revHead
            revHead = curr
            curr = temp
        return revHead