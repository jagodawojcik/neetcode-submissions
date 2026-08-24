# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        def mergeList(l1, l2) -> ListNode:
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
                l1 = l1.next
                cur = cur.next
            
            while l2:
                cur.next = l2
                l2 = l2.next
                cur = cur.next

            return dummy.next


        if not lists or len(lists) == 0:
            return None

        while len(lists) > 1:
            merged_lists = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                if i + 1 >= len(lists):
                    merged_lists.append(l1)
                    continue
                l2 = lists[i+1]
                merged_lists.append(mergeList(l1, l2))
            lists = merged_lists
        
        return lists[0]


        



            

        



