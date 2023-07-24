from typing import * 

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    
        def toNum(nums): 
            num = 0 
            n = len(nums)
            order = 1 
            for i in range(n-1,-1,-1): 
                num += nums[i] * order 
                order *= 10 
            return num 
        
        def LNtoNum(head):
            nums = [head.val] 
            node = head
            while node.next: 
                node = node.next 
                nums.append(node.val) 
            num = toNum(nums)
            return num 
        
        num1 = LNtoNum(l1)
        num2 = LNtoNum(l2)
        ans = num1 + num2
        
        if ans == 0: 
            return ListNode(0)
         
        nums = []
        while ans > 0: 
            nums.append(ans%10)
            ans //= 10 
        
        n = len(nums)
        head = ListNode(nums[-1])
        node = head 
        for i in range(n-2,-1,-1): 
            node.next = ListNode(nums[i])
            node = node.next 
        
        return head 
            
