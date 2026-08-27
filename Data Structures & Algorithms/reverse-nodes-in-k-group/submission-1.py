# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def get_kth(curr, k):
            while curr and k > 0:
                curr = curr.next
                k -= 1      
            return curr

        
        dummy = ListNode()
        dummy.next = head
        prev_group = dummy
        while True:
            kth = get_kth(prev_group, k)
            if not kth:
                break

            next_group = kth.next # because kth.next is getting updated in reverse op
            prev = kth.next
            cur = prev_group.next

            while cur != next_group:
                tmp = cur.next
                cur.next = prev
                prev = cur
                cur = tmp
            
            tmp = prev_group.next
            prev_group.next = kth
            prev_group = tmp

        return dummy.next






