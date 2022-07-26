import random 

class Node:
    def __init__(self, val=-1, right=None, down=None): 
        self.val = val 
        self.right = right 
        self.down = down 

class Skiplist:

    def __init__(self):
        # dummy head 
        self.head = Node()

    def search(self, target: int) -> bool:
        node = self.head 
        while node: 
            # move right 
            while node.right and node.right.val < target: 
                node = node.right 
            if node.right and node.right.val == target:
                return True 
            # move down 
            node = node.down 
        return False 

    def add(self, num: int) -> None:
        nodes = []
        node = self.head 
        while node: 
            # move right 
            while node.right and node.right.val < num: 
                node = node.right 
            nodes.append(node)
            # move down 
            node = node.down 

        # insert from bottom to up 
        insert = True 
        down = None 
        while insert and nodes: 
            node = nodes.pop()
            node.right = Node(num, node.right, down)
            down = node.right 
            # toss a coin, note that only need to toss once 
            insert = (random.getrandbits(1) == 0)
        
        # create a new level with a dummy head 
        if insert: 
            self.head = Node(-1, None, self.head)
            


    def erase(self, num: int) -> bool:
        node = self.head 
        found = False 
        while node: 
            # move right 
            while node.right and node.right.val < num: 
                node = node.right 
            if node.right and node.right.val == num:
                # delete, cannot return since we need to delete in lower layers 
                node.right = node.right.right 
                found = True 
            # move down 
            node = node.down 
        return found 
