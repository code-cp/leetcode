# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import * 

class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr = []
        node = head 
        while node is not None: 
            arr.append(node.val)
            node = node.next 
            
        head = None 
        if len(arr) == 1 and arr[0] == 0: 
            return head  
        
        def removeSum():
            nonlocal arr  
            n = len(arr) 
            prefix = [0]*(n+1)
            for i in range(n): 
                prefix[i+1] = prefix[i] + arr[i]
            for i in range(n): 
                # NOTE, j is not range(i+1, n)
                for j in range(i, n):
                    total = prefix[j+1] - prefix[i]
                    if total == 0: 
                        # exclude [i,j]
                        arr = arr[:i] + arr[j+1:]
                        return 
            return 
        
        stop = False 
        while not stop: 
            stop = True
            n = len(arr)
            removeSum()
            m = len(arr)
            if n != m:
                stop = False  

        if len(arr) > 0:
            head = ListNode(arr[0])
            node = head
            for i in range(1, len(arr)):
                node.next = ListNode(arr[i])
                node = node.next   
        
        return head   
    
if __name__ == "__main__": 
    s = Solution() 

    head = ListNode(2)
    head.next = ListNode(0)
    s.removeZeroSumSublists(head)

    # head = ListNode(1)
    # head.next = ListNode(3)
    # head.next.next = ListNode(2)
    # head.next.next.next = ListNode(-3)
    # head.next.next.next.next = ListNode(-2) 
    # head.next.next.next.next.next = ListNode(5) 
    # head.next.next.next.next.next.next = ListNode(5) 
    # head.next.next.next.next.next.next.next = ListNode(-5) 
    # head.next.next.next.next.next.next.next.next = ListNode(1) 
    # s.removeZeroSumSublists(head)
    
    # head = ListNode(1)
    # head.next = ListNode(-1)
    # s.removeZeroSumSublists(head)

    # head = ListNode(1)
    # head.next = ListNode(2)
    # head.next.next = ListNode(-3)
    # head.next.next.next = ListNode(3)
    # head.next.next.next.next = ListNode(1) 
    # s.removeZeroSumSublists(head)
            
            