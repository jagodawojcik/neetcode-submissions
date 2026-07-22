# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        # Find the middle node
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next # middle node
            fast = fast.next.next
        
        # slow: 2 -> 4 -> 6 -> None
        half_list = slow.next # 8
        slow.next = None
        prev = None
        while half_list:
            next_node = half_list.next
            half_list.next = prev
            prev = half_list
            half_list = next_node
        
        # half_list: 10 -> 8 -> None
        # prev: 10

        # 2 -> 10 -> 4
        first, half_list = head, prev
        while half_list:
            tmp1, tmp2 = half_list.next, first.next
            first.next = half_list
            half_list.next = tmp2

            half_list = tmp1
            first = tmp2
            

        










