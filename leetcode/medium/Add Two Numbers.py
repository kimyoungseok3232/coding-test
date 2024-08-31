# https://leetcode.com/problems/add-two-numbers/
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        sumlist = ListNode(0)
        head = sumlist
        up = 0
        while l1 and l2:
            vsum = l1.val + l2.val + up
            up = vsum//10
            sumlist.next = ListNode(vsum%10)
            sumlist = sumlist.next
            l1, l2 = l1.next, l2.next
        while l1:
            vsum = l1.val + up
            up = vsum//10
            sumlist.next = ListNode(vsum%10)
            sumlist = sumlist.next
            l1 = l1.next
        while l2:
            vsum = l2.val + up
            up = vsum//10
            sumlist.next = ListNode(vsum%10)
            sumlist = sumlist.next
            l2 = l2.next
        if up:
            sumlist.next = ListNode(up)
        return head.next