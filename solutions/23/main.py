from typing import * 
import heapq 

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        n = len(lists)
        cur_nodes = [head for head in lists] 
        nodes = []
        dummy = ListNode()
        cur = dummy 
        
        while len(cur_nodes) > 0:
            for i, c in enumerate(cur_nodes):
                if c is not None: 
                    heapq.heappush(nodes, c.val)
                    cur_nodes[i] = c.next
            cur_nodes = [c for c in cur_nodes if c is not None]

        while len(nodes) > 0:
            cur.next = ListNode(heapq.heappop(nodes))
            cur = cur.next 
                
        return dummy.next 
                