from typing import * 
from collections import deque 

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        values = []
        node = head 
        while node is not None: 
            values.append(node.val)
            node = node.next 
        n = len(values)
        ans = [0]*n
        stack = deque()
        for i in range(n-1,-1,-1):
            while len(stack) > 0 and values[i] >= stack[-1]: 
                stack.pop()
            if len(stack) == 0: 
                stack.append(values[i])
                continue 
            ans[i] = stack[-1] 
            stack.append(values[i]) 
        return ans 
                 
if __name__ == "__main__": 
    s = Solution() 
   
    head = ListNode(9)
    values = [7,6,7,6,9]
    node = head 
    for i in range(len(values)): 
        cur = ListNode(values[i])
        node.next = cur 
        node = cur 
    assert s.nextLargerNodes(head)  == [0,9,7,9,9,0]   
    
    # head = ListNode(2)
    # head.next = ListNode(1)
    # head.next.next = ListNode(5)
    # assert s.nextLargerNodes(head)  == [5,5,0]              