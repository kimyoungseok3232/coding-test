# https://leetcode.com/problems/swap-nodes-in-pairs/description/
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next: return head

        prev = ListNode(0)
        sw = prev
        v = head.next
        while head and head.next and v:
            v = head.next
            prev.next = v
            head.next = v.next
            v.next = head
            prev = head
            head = head.next
        if head:
            prev.next = head
        return sw.next