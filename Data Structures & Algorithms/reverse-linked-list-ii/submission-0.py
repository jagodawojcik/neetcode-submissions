# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        
        dummy = ListNode()
        dummy.next = head

# [1,2,3,4,5] l = 1, r = 3

        # Locate left_node - 1
        left_prev = dummy
        for _ in range(left - 1):
            left_prev = left_prev.next

        # Reverse sublist (from l to r)
        prev = None
        left_node = left_prev.next
        sublist = left_prev.next
        for _ in range(right-left + 1):
            tmp = sublist.next
            sublist.next = prev
            prev = sublist
            sublist = tmp

        left_prev.next = prev
        left_node.next = sublist

        return dummy.next
       
        

        

