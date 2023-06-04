# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        cont_set = set()
        cur = head
        while cur:
            if cur in cont_set:
                return True
            cont_set.add(cur)
            cur = cur.next
        return False
