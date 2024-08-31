# https://leetcode.com/problems/reverse-linked-list/
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
def reverse(head):
    if head.next.next:
        tail = reverse(head.next)
    else:
        tail = head.next
    head.next.next = head
    head.next = None
    return tail
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head and head.next:
            return reverse(head)

        return head