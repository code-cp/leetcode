from typing import * 
from collections import deque 
class LockingTree:

    def __init__(self, parent: List[int]):
        self.parent = parent 
        n = len(parent)
        # locked or not, user id 
        self.status = [[0]*2 for _ in range(n)]

        self.adj = [[] for _ in range(n)]
        for i, p in enumerate(parent): 
            # NOTE, skip root 
            if p == -1: 
                continue 
            self.adj[p].append(i)

    def lock(self, num: int, user: int) -> bool:
        if self.status[num][0] == 1: 
            return False 
        self.status[num][0] = 1 
        self.status[num][1] = user 
        return True  

    def unlock(self, num: int, user: int) -> bool:
        if self.status[num][0] == 0: 
            return False 
        elif self.status[num][1] != user: 
            return False 
        self.status[num][0] = 0 
        self.status[num][1] = 0 
        return True 

    def upgrade(self, num: int, user: int) -> bool:
        # check whether itself and its ancestors are locked 
        cur = num 
        if self.status[cur][0] == 1: 
            return False 
        while self.parent[cur] != -1: 
            cur = self.parent[cur]
            if self.status[cur][0] == 1: 
                return False 

        valid = False 
        decendants = []
        q = deque([num])
        while len(q) > 0: 
            q_len = len(q)
            for _ in range(q_len):
                node = q.popleft()
                if self.status[node][0] == 1: 
                    valid = True 
                    decendants.append(node)  
                [q.append(i) for i in self.adj[node]]
                
        if valid:
            # NOTE, use num not cur 
            self.status[num][0] = 1 
            self.status[num][1] = user
            for i, node in enumerate(decendants):
                self.status[node][0] = 0 
                self.status[node][1] = 0  

        return valid 
             
if __name__ == "__main__": 
    # obj = LockingTree([-1,0,0,1,1,2,2])
    
    # assert obj.lock(2,2)
    # assert not obj.unlock(2,3)
    # assert obj.unlock(2,2)
    # assert obj.lock(4,5)
    # assert obj.upgrade(0,1)
    # assert not obj.lock(0,1)

    obj = LockingTree([-1,4,9,0,6,1,0,6,3,1])
    obj.upgrade(9,43)
    obj.upgrade(4,27)
    obj.upgrade(5,34)
    obj.upgrade(7,31)
    obj.upgrade(4,27)
    obj.lock(2,47)
    obj.unlock(7,21)
    obj.upgrade(4,12)
    obj.upgrade(1,1)
    obj.upgrade(8,20)
    obj.lock(5,50)
    obj.upgrade(5,28)
    assert obj.upgrade(0,11)