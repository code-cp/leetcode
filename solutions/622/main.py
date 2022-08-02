class MyCircularQueue:

    def __init__(self, k: int):
        self.que = [-1] * k  
        self.n = k 
        self.start = 0
        self.end = 0

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False 

        self.que[self.end] = value
        self.end += 1 
        self.end %= self.n
        return True 

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False

        self.que[self.start] = -1 
        self.start += 1 
        self.start %= self.n
        return True 

    def Front(self) -> int:
        if self.isEmpty():
            return -1

        return self.que[self.start]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1

        return self.que[self.end-1]

    def isEmpty(self) -> bool:
        return self.start == self.end and self.que[self.start] == -1 

    def isFull(self) -> bool:
        return self.end == self.start and self.que[self.start] != -1 

if __name__ == "__main__": 
    myCircularQueue = MyCircularQueue(3)
    assert myCircularQueue.enQueue(1)# return True
    assert myCircularQueue.enQueue(2)# return True
    assert myCircularQueue.enQueue(3)# return True
    assert not myCircularQueue.enQueue(4)# return False
    assert myCircularQueue.Rear() == 3  # return 3
    assert myCircularQueue.isFull()  # return True
    assert myCircularQueue.deQueue() # return True
    assert myCircularQueue.enQueue(4)# return True
    assert myCircularQueue.Rear() == 4  # return 4

