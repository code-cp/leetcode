# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

import random 
random.seed(0)
from typing import Optional

class Solution:
    def __init__(self, head: Optional[ListNode]):
        self.head = head
    def getRandom(self) -> int:
        result = self.head.val
        cur = self.head
        count = 0
        while cur:
            if random.randint(0, count) == 0:
                result = cur.val
            count += 1
            cur = cur.next
        return result

if __name__ == "__main__": 
    head = ListNode(0)
    head.next = ListNode(1)

    obj = Solution(head)
    param_1 = obj.getRandom()
    print(param_1)
