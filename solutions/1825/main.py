from sortedcontainers import SortedList 
from collections import deque 
class MKAverage:

    def __init__(self, m: int, k: int):
        self.m = m 
        self.k = k 
        self.sum = 0 
        self.q = deque()

        self.left = SortedList()
        self.mid = SortedList()
        self.right = SortedList()

    def addElement(self, num: int) -> None:
        if len(self.q) < self.m: 
            self.q.append(num)
            self.mid.add(num)
            self.sum += num 
            if len(self.q) == self.m: 
                while len(self.left) < self.k: 
                    self.sum -= self.mid[0]
                    self.shiftLeft(self.left, self.mid)
                while len(self.right) < self.k: 
                    self.sum -= self.mid[-1]
                    self.shiftRight(self.mid, self.right)
        elif len(self.q) == self.m:
            self.q.append(num)
            if num <= self.left[-1]:
                self.left.add(num)
            elif num >= self.right[0]: 
                self.right.add(num)
            else: 
                self.mid.add(num)
                self.sum += num 

            if len(self.left) > self.k: 
                self.sum += self.left[-1]
                self.shiftRight(self.left, self.mid) 
            if len(self.right) > self.k: 
                self.sum += self.right[0]
                self.shiftLeft(self.mid, self.right)

            x = self.q.popleft()
            if x <= self.left[-1]: 
                self.left.pop(self.left.index(x))
            elif x >= self.right[0]:
                self.right.pop(self.right.index(x))
            else: 
                self.mid.pop(self.mid.index(x))
                self.sum -= x 

            if len(self.left) < self.k: 
                self.sum -= self.mid[0]
                self.shiftLeft(self.left, self.mid)
            if len(self.right) < self.k:
                self.sum -= self.mid[-1]
                self.shiftRight(self.mid, self.right)

    def calculateMKAverage(self) -> int:
        if len(self.q) < self.m: 
            return -1
        else: 
            return self.sum // (self.m - self.k*2)

    def shiftLeft(self, set1, set2): 
        set1.add(set2[0])
        set2.pop(0)

    def shiftRight(self, set1, set2): 
        set2.add(set1[-1])
        set1.pop(len(set1)-1)

if __name__ == "__main__": 
    s = MKAverage(3, 1)
    s.addElement(3)
    s.addElement(1)
    s.addElement(10)
    assert s.calculateMKAverage() == 3 

