# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # traverse for k-1
        # append those k-1 nodes into a stack
        # the kth node will be the start of the new order
        # kth.next => stack.pop()
        # if the last thing popped from the stack == head then the cur start of that sublist will be the new head
        # keep track of the last thing popped because its next will be the beginning of the new reversed list
        # if eventually len(stack) < k and no more nodes, dont reverse and just return beginning of the stack
        # stack = [5] 2->1->4->3 -> 5

        
        cur2 = head
        newStart = ListNode(10**5)
        cur = newStart
        while cur2:
            
            stack = []
            while len(stack) < k and cur2: #Stack nodes till k-1
                stack.append(cur2)
                print(f"{stack[-1].val=}")
                cur2 = cur2.next
            print("stack done")
            #print(f"{stack=}")
            if len(stack) < k: #couldnt finish the entire k
                print("hit")
                newStart.next = stack[0]
            else:
                temp = cur2.next if cur2 else None #Hold what was after k
                while stack:
                    newStart.next = stack.pop()
                    newStart = newStart.next
                newStart.next = temp
                #cur2 =  newStart.next
            
        return cur.next