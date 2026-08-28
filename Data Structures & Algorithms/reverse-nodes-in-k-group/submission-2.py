# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        def find_kth(cur, k):    
            while k > 0 and cur:
                cur = cur.next
                k -= 1
            return cur


        dummy = ListNode()
        dummy.next = head
        prev_group = dummy 

        while True:
            kth = find_kth(prev_group, k)
            if not kth:
                break

            cur, prev = prev_group.next, kth.next
            next_group = kth.next
            while cur != next_group:
                tmp = cur.next
                cur.next = prev
                prev = cur
                cur = tmp

            tmp = prev_group.next
            prev_group.next = kth
            prev_group = tmp


        return dummy.next
        
