# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        size = 0
        i = 0
        cur = head
        d_cur = cur
        while d_cur:
            size += 1
            d_cur = d_cur.next
        middle = size // 2 
        while cur:
            if i == middle:
                return cur
            i += 1
            cur = cur.next
