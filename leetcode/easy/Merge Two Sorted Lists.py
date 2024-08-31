# https://leetcode.com/problems/merge-two-sorted-lists/description/
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode(-101)
        merged = head
        while list1 and list2:
            if list1.val <= list2.val:
                merged.next = list1
                list1 = list1.next
            else:
                merged.next = list2
                list2 = list2.next
            merged = merged.next
            
        if list1:
            merged.next = list1
        elif list2:
            merged.next = list2
        return head.next
