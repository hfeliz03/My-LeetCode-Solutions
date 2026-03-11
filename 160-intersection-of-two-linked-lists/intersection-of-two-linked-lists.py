# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        pA = headA
        pB = headB

        while pA != pB:
            pA = headB if pA is None else pA.next
            pB = headA if pB is None else pB.next

        return pA
        # nodes_in_B = set()

        # while headB is not None:
        #     nodes_in_B.add(headB)
        #     headB = headB.next

        # while headA is not None:
        #     # if we find the node pointed to by headA,
        #     # in our set containing nodes of B, then return the node
        #     if headA in nodes_in_B:
        #         return headA
        #     headA = headA.next

        # return None