from typing import * 

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head 
        cur = dummy 
        
        while cur.next is not None and cur.next.next is not None: 
            # swap two nodes 
            next_node = cur.next 
            next_next_node = cur.next.next 
            next_head = cur.next.next.next 
            
            next_next_node.next = next_node 
            next_node.next = next_head 
           
            cur.next = next_next_node  
            cur = cur.next.next 
            
        return dummy.next 