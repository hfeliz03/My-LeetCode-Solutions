# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        #find the tail, and prevtail
        #make tail.next = head
        #make head = tail
        #make prevtail.next = none
        #loop k times
        cur = head
        n = 0
        while cur:
            cur = cur.next
            n += 1
        if not head or n == k: return head
        k %= n

        def findTailAndPrev(head):
            cur = head
            prev = None
            while cur.next:
                prev = cur
                cur = cur.next
            return prev, cur

        cur = head
        for _ in range(k):
            prev, tail = findTailAndPrev(cur)
            tail.next = head
            head = tail
            prev.next = None

        return head

        #while finding for tail, if lenlist == k just return head