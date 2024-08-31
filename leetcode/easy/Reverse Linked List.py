# https://leetcode.com/problems/reverse-linked-list/
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