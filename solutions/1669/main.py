from tying import * 

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        cur1 = list1 
        i = 1 
        while i < a: 
            i += 1 
            cur1 = cur1.next 
        cur2 = cur1 
        while i <= b: 
            i += 1 
            cur1 = cur1.next 
        cur1 = cur1.next 

        cur2.next = list2
        cur2 = cur2.next 
        while cur2.next:
            cur2 = cur2.next 
        cur2.next = cur1 

        return list1 


         
