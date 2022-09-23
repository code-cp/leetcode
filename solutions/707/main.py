class Node:
    def __init__(self, val, pre, nex): 
        self.val = val 
        self.pre = pre 
        self.nex = nex 

class MyLinkedList:

    def __init__(self):
        self.head = Node(-1, None, None)
        self.tail = Node(-1, None, None)
        self.head.nex = self.tail 
        self.tail.pre = self.head 
        self.len = 0 

    def get(self, index: int) -> int:
        if index < 0 or index >= self.len: 
            return -1 
        node = self.head 
        while index >= 0: 
            node = node.nex 
            index -= 1 
        return node.val 

    def addAtHead(self, val: int) -> None:
        node = Node(val, self.head, self.head.nex)
        self.head.nex.pre = node 
        self.head.nex = node 
        self.len += 1 

    def addAtTail(self, val: int) -> None:
        node = Node(val, self.tail.pre, self.tail)
        self.tail.pre.nex = node 
        self.tail.pre = node 
        self.len += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.len:
            return 
        self.len += 1
        node = self.head 
        while index > 0: 
            node = node.nex 
            index -= 1 
        new_node = Node(val, node, node.nex)
        node.nex.pre = new_node
        node.nex = new_node 

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.len: 
            return 
        self.len -= 1
        node = self.head 
        while index >= 0: 
            node = node.nex 
            index -= 1 
        node.pre.nex = node.nex 
        node.nex.pre = node.pre 