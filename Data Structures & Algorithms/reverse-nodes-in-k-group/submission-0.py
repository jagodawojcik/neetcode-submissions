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
        prev_group = dummy # one node before the subgroup

        while True:
            kth = get_kth(prev_group, k)
            if not kth:
                break

            next_group = kth.next # one node after the subgroup

            # reverse the subgroup
            # prev is kth.next because it points to the next subgroup
            # curr is first node of the subgroup
            prev, curr = kth.next, prev_group.next
            while curr != next_group:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp

            tmp = prev_group.next
            prev_group.next = kth
            prev_group = tmp

        return dummy.next




