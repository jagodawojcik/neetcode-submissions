# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        

        dummy = ListNode()

        seq = dummy
        while list1 and list2:
            if list1.val < list2.val:
                seq.next = list1
                list1 = list1.next
            else:
                seq.next = list2
                list2 = list2.next
            seq = seq.next

        while list1:
            seq.next = list1
            list1 = list1.next
            seq = seq.next

        while list2:
            seq.next = list2
            list2 = list2.next
            seq = seq.next


        return dummy.next