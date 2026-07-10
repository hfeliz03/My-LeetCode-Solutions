# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        curr = head
        dummy = ListNode("dummy", curr)
        prev = dummy
        while curr:
            print(curr.val)
            if curr.val == val:
                print("hit")
                prev.next = curr.next    
            else:
                prev = prev.next
            curr = curr.next
        return dummy.next