from typing import * 

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def gcd(a, b): 
            while b > 0:
                a, b = b, a % b 
            return abs(a)  
        
        dummy = ListNode(val=0, next=head)
        cur = dummy 
        while cur.next is not None and cur.next.next is not None: 
            add_val = gcd(cur.next.val, cur.next.next.val)
            add_node = ListNode(add_val)
            add_node.next = cur.next.next 
            cur.next.next = add_node
            cur = cur.next.next
            
        return head 
            
        