# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next  : return False
        oneStep, twoStep = head, head.next
        while twoStep and twoStep.next:
            if oneStep == twoStep : return True
            else: 
                oneStep = oneStep.next
                twoStep = twoStep.next.next
        return False