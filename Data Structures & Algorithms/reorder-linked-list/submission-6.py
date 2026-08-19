# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # find middle node
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        middle = slow.next
        slow.next = None
        prev = None
        while middle:
            tmp = middle.next
            middle.next = prev
            prev = middle
            middle = tmp

        middle = prev
        while middle:
            tmp1, tmp2 = head.next, middle.next
            
            head.next = middle
            middle.next = tmp1

            head = tmp1
            middle = tmp2
        


        









