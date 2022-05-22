from typing import * 

class ListNode(): 
    def __init__(self, val=0, next=None): 
        self.val = val 
        self.next = next 

class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        if k == 1: 
            return n 

        next_node = ListNode(1, None)
        root = next_node 
        for i in range(n, 1, -1): 
            cur_node = ListNode(i, next_node)
            next_node = cur_node 
        root.next = next_node
        total = n 
        while total != 1: 
            count = k - 1 
            while count: 
                prev = root 
                root = root.next 
                count -= 1 
            total -= 1 
            prev.next = prev.next.next 
            root = prev.next
        return root.val 

if __name__ == "__main__": 
    s = Solution() 

    n = 3
    k = 1
    result = s.findTheWinner(n, k) 
    assert result == 3 

    n = 5
    k = 2
    result = s.findTheWinner(n, k) 
    assert result == 3 

    n = 6
    k = 5
    result = s.findTheWinner(n, k) 
    assert result == 1 