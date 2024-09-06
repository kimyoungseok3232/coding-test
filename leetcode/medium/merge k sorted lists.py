# https://leetcode.com/problems/merge-k-sorted-lists/description/
from typing import Optional, List
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        node = []
        for l in lists:
            while l:
                node.append(l.val)
                l = l.next
        node = sorted(node)
        head = ListNode(0)
        res = head
        for n in node:
            ln = ListNode(n)
            head.next = ln
            head = head.next
        return res.next

import heapq
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        node = []
        for l in range(len(lists)):
            if lists[l]:
                heapq.heappush(node,[lists[l].val,l])
        
        res = head = ListNode(0)
        while node:
            idx = heapq.heappop(node)[1]
            head.next = lists[idx]
            head, lists[idx] = head.next, lists[idx].next
            if lists[idx]:
                heapq.heappush(node,[lists[idx].val,idx])
        
        return res.next