from typing import * 

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        traversed = set()
        node = head 
        if node is None: 
            return False 
        traversed.add(node)
        while node.next:
            node = node.next 
            if node in traversed: 
                return True 
            traversed.add(node)
        return False 
             
            