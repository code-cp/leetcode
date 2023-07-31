from typing import * 

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
        
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        nodes = {}
        i = 0 
        cur = head 
        while cur is not None: 
            nodes[i] = cur 
            cur = cur.next 
            i += 1 
        
        j = 0 
        cur = head
        pre = None  
        while j < i: 
            pre = cur 
            if j % 2 == 0: 
                # NOTE, j//2 
                cur.next = nodes[i-j//2-1]
            else: 
                cur.next = nodes[(j+1)//2] 
            j += 1 
            cur = cur.next 
        # don't forget this 
        pre.next = None 
            
        return head 
        
if __name__ == "__main__": 
    s = Solution()
    
    head = ListNode(1) 
    head.next = ListNode(2) 
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    s.reorderList(head)     