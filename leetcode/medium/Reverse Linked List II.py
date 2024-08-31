# https://leetcode.com/problems/reverse-linked-list-ii/description/
def reverse(head):
    if head.next.next:
        tail , _ = reverse(head.next)
    else:
        tail = head.next
    head.next.next = head
    head.next = None
    return tail, head
    
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or not head.next or left==right: return head

        res = head
        for i in range(left-1):
            head_end = head
            head = head.next
    
        tail = head
        for i in range(right-left):
            tail = tail.next
        overtail = tail.next
        tail.next = None

        head, tail = reverse(head)

        tail.next = overtail

        if left == 1:
            return head
        
        head_end.next = head
        return res