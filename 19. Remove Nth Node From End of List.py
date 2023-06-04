# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        i = 0
        prev = None
        cur = head
        found = False
        dumy_cur = cur
        size = 0
        while dumy_cur:
            size += 1
            dumy_cur = dumy_cur.next
        while cur:
            if size - i == n:
                found = True
                break
            prev = cur
            cur = cur.next
            i += 1
        if found: 
            if not prev: head = head.next
            else: prev.next = cur.next
        return head
