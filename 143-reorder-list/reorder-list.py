# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return

        # Step 1: Find middle
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Disconnect first and second halves
        second = slow.next
        slow.next = None

        # Step 2: Reverse second half
        revHead = None
        currInv = second
        while currInv:
            temp = currInv.next
            currInv.next = revHead
            revHead = currInv
            currInv = temp

        # Step 3: Merge two halves
        curr, revCurr = head, revHead
        while revCurr:
            tempFront = curr.next
            tempBack = revCurr.next
            curr.next = revCurr
            revCurr.next = tempFront
            curr = tempFront
            revCurr = tempBack
