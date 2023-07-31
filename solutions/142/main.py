from typing import * 

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow, fast = head, head 
        while fast is not None and fast.next is not None and fast.next != slow: 
            slow = slow.next 
            fast = fast.next.next 
        # no cycle 
        if fast is None or fast.next is None: 
            return None 
        
        # find intersection, ref 160 
        # one linked list starts at head, one starts at slow 
        cur1, cur2 = head, slow 
        end = fast 
        while cur1 != cur2: 
            if cur1 == end: 
                cur1 = slow 
            else: 
                cur1 = cur1.next 
            if cur2 == end: 
                cur2 = head 
            else: 
                cur2 = cur2.next 
            
        return cur1 