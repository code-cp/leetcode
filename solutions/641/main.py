from typing import * 

class MyCircularDeque:

    def __init__(self, k: int):
        self.max_len = k 
        self.start = 0 
        self.end = 0
        self.data = [-1] * k 
        self.num = 0 

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False 
        self.num += 1 
        self.data[self.start] = value

        if not self.isFull() and self.start == self.end: 
            self.end += 1 
            self.end %= self.max_len 

        self.start -= 1 
        if self.start == -1: 
            self.start = self.max_len-1  
        return True 

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False   
        self.num += 1  
        self.data[self.end] = value

        if not self.isFull() and self.start == self.end: 
            self.start -= 1 
            if self.start == -1: 
                self.start = self.max_len-1

        self.end += 1 
        self.end %= self.max_len 
        return True 

    def deleteFront(self) -> bool:
        if self.isEmpty(): 
            return False 
        self.num -= 1
        self.start += 1 
        self.start %= self.max_len
        self.data[self.start] = -1
        return True 

    def deleteLast(self) -> bool:
        if self.isEmpty(): 
            return False 
        self.num -= 1 
        self.end -= 1 
        if self.end == -1: 
            self.end = self.max_len-1  
        self.data[self.end] = -1
        return True 

    def getFront(self) -> int:
        if self.isEmpty():
            return -1 
        idx = self.start+1 
        idx %= self.max_len 
        return self.data[idx]

    def getRear(self) -> int:
        if self.isEmpty():
            return -1 
        idx = self.end-1 
        if idx == -1: 
            idx = self.max_len-1 
        return self.data[idx]

    def isEmpty(self) -> bool:
        return self.num == 0  

    def isFull(self) -> bool:
        return self.num == self.max_len 

if __name__ == "__main__": 
    # s = MyCircularDeque(3)
    # assert s.insertLast(1)
    # assert s.insertLast(2)
    # assert s.insertFront(3)
    # assert not s.insertFront(4)
    # assert s.getRear() == 2
    # assert s.isFull()
    # assert s.deleteLast()
    # assert s.insertFront(4)
    # assert s.getFront() == 4 

    s = MyCircularDeque(5)
    assert s.insertFront(7)
    assert s.insertLast(0)
    assert s.getFront() == 7

    