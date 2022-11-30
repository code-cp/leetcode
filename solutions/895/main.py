from collections import deque 
class FreqStack:

    def __init__(self):
        self.cnt = {}
        self.max_cnt = 0 
        self.groups = {}

    def push(self, val: int) -> None:
        cnt = self.cnt.get(val, 0)+1 
        self.cnt[val] = cnt 
        if cnt > self.max_cnt: 
            self.max_cnt = cnt 
            self.groups[cnt] = deque()
        self.groups[cnt].append(val)
          
    def pop(self) -> int:
        res = self.groups[self.max_cnt].pop()
        self.cnt[res] -= 1 
        if not self.groups[self.max_cnt]:
            self.max_cnt -= 1 
        return res 


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()