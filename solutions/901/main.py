
from collections import deque 
class StockSpanner:

    def __init__(self):
        self.num_stack = deque()
        self.cnt_stack = deque()

    def next(self, price: int) -> int:
        if len(self.num_stack) == 0 or price < self.num_stack[-1]: 
            self.num_stack.append(price)
            self.cnt_stack.append(1)
            return 1 
        res = 1
        while self.num_stack and price >= self.num_stack[-1]: 
            self.num_stack.pop()
            count = self.cnt_stack.pop()
            res += count 
        self.num_stack.append(price)
        self.cnt_stack.append(res)
        return res 

if __name__ == "__main__": 
    s = StockSpanner()
    assert s.next(100) == 1 
    assert s.next(80) == 1 
    assert s.next(60) == 1
    assert s.next(70) == 2  









