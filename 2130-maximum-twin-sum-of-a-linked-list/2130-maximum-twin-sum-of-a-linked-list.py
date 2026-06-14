# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        curMax = -10**5
        vals = []
        curNode = head
        n = 0
        while curNode:
            n+=1
            curNode = curNode.next
        
        print(n)

        curNode = head
        i = 0
        while i <= (n/2) - 1:
            vals.append(curNode.val)
            curNode = curNode.next
            i += 1
        
        print(i)
        print(vals)
        j = 0
        while j + i < n:
            print(curMax)
            vals[i - j - 1] += curNode.val
            curMax = max(vals[i-j - 1], curMax)
            curNode = curNode.next
            j+=1



        return curMax