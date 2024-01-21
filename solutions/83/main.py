from typing import * 

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        elements = set()
        dummy = ListNode()
        dummy.next = head 
        node = dummy 
        while node.next: 
            while node.next is not None and node.next.val in elements:
                node.next = node.next.next 
            if node.next is not None: 
                elements.add(node.next.val)
                node = node.next 
            else: 
                return dummy.next 
        return dummy.next 