from collections import deque 
class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.q = deque()
        self.n = size 
        self.pre_mean = 0 

    def next(self, val: int) -> float:
        n = len(self.q) 
        self.q.append(val)
        l = 0 
        if len(self.q) > self.n:
            l = self.q.popleft()
        # mean = sum / n 
        # sum = mean * n 
        # new sum = sum - a + b 
        # new mean = new sum / n 
        old_sum = self.pre_mean * n 
        new_sum = old_sum - l + val 
        mean = new_sum / len(self.q) 
        self.pre_mean = mean 
        return mean 



