# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr1, curr2, carryOne = l1, l2, False
        dummy = ListNode()
        dummyCurr = dummy

        while curr1 and curr2:
            sumVal = (curr1.val + curr2.val)
            if carryOne == True: sumVal +=1
            ListNode((sumVal )%10)
            dummyCurr.next = ListNode(sumVal%10)
            carryOne = True if sumVal >= 10 else False
            dummyCurr = dummyCurr.next
            curr1, curr2 = curr1.next, curr2.next
        while curr1:
            val = curr1.val
            if carryOne == True: val+=1
            carryOne = True if val >= 10 else False
            dummyCurr.next = ListNode(val%10)
            dummyCurr = dummyCurr.next
            curr1 = curr1.next
            print(val)
        while curr2:
            val = curr2.val
            if carryOne == True: val+=1
            carryOne = True if val >= 10 else False
            dummyCurr.next = ListNode(val%10)
            dummyCurr = dummyCurr.next
            curr2 = curr2.next
        if carryOne == True: dummyCurr.next = ListNode(1)
        return dummy.next