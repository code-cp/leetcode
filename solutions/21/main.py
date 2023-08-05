from typing import * 

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        cur = ListNode()  
        head = cur 
        
        cur1 = list1 
        cur2 = list2 
        while cur1 is not None and cur2 is not None: 
            if cur1.val < cur2.val: 
                cur.next = cur1 
                cur1 = cur1.next 
            else: 
                cur.next = cur2 
                cur2 = cur2.next 
            cur = cur.next 
                
        while cur1 is not None: 
            cur.next = cur1 
            cur1 = cur1.next 
            cur = cur.next 
            
        while cur2 is not None: 
            cur.next = cur2 
            cur2 = cur2.next 
            cur = cur.next 
            
        return head.next 