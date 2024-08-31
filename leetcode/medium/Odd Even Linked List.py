# https://leetcode.com/problems/odd-even-linked-list/description/
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return head
        if not head.next: return head
        if not head.next.next: return head
        res = head
        ehead = head.next
        while head and head.next and head.next.next:
            odd = head
            even = head.next
            odd.next = odd.next.next
            even.next = even.next.next
            head = odd.next
        head.next = ehead
        return res

