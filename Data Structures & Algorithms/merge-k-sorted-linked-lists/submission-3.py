# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        def merge_list(l1, l2):
            dummy = ListNode()
            cur = dummy 

            while l1 and l2:
                if l1.val < l2.val:
                    cur.next = l1
                    l1 = l1.next
                else:
                    cur.next = l2
                    l2 = l2.next
                cur = cur.next

            while l1:
                cur.next = l1
                cur = cur.next
                l1 = l1.next
            while l2:
                cur.next = l2
                cur = cur.next
                l2 = l2.next
                
            return dummy.next

        if len(lists) == 0:
            return None

        while len(lists) > 1:
            merged_lists = []

            for i in range(0, len(lists), 2):
                if i + 1 >= len(lists):
                    merged_lists.append(lists[i])
                    continue
                l = merge_list(lists[i], lists[i+1])
                merged_lists.append(l)

            lists = merged_lists

        return lists[0]
        