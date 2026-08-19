# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        

       
        arr = []
        cur = head
        while cur:
            arr.append(cur)
            cur = cur.next

        num_nodes = len(arr)

        for i in range(len(arr) // 2):
            tmp = head.next
            head.next = arr[-(i + 1)]
            head.next.next = tmp
            head = head.next.next

        if num_nodes > 1:
            tmp.next = None






