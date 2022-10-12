from typing import * 

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:
        components = []
        node = head
        while node: 
            if node.val in nums: 
                components.append(1)
            else: 
                components.append(0)
            node = node.next 
        res = 0 
        count = 0 
        for c in components: 
            count += c 
            if c == 0: 
                if count > 0: 
                    res += 1 
                count = 0 
        if count > 0: 
            res += 1 
        return res 


