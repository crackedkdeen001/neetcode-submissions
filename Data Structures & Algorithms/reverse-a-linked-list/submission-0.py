# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        actual_head = None
        while head:
            tmp = head.next
            head.next = prev
            prev = head

            if tmp is None: 
                actual_head = head

            head = tmp

        return actual_head