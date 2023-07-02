from typing import * 

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:  
        
        def getNum(head): 
            num = 0 
            order = 1
            node = head 
            while node: 
                num += order * node.val 
                node = node.next 
                order *= 10 
            return num 
        
        n1 = getNum(l1)
        n2 = getNum(l2)
        ans = n1 + n2 
        
        head = ListNode(0)
        node = head  
        while ans > 0:
            node.val = ans % 10 
            ans //= 10 
            if ans > 0:
                node.next = ListNode(0) 
                node = node.next 
                
        return head 
            