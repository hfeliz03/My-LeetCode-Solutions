# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        ptr = dummy

        curr1 , curr2 = list1, list2
        while (curr1 is not None and curr2 is not None):
            if curr1.val < curr2.val :
                ptr.next = curr1
                curr1 = curr1.next
            else: 
                ptr.next = curr2
                curr2 = curr2.next
            ptr = ptr.next

        if curr1 is None:
            ptr.next = curr2
        if curr2 is None:
            ptr.next = curr1

        return dummy.next