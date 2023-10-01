from collections import defaultdict 

class Node: 
    def __init__(self, key, val, pre=None, nex=None, freq=0): 
        self.pre = pre 
        self.nex = nex 
        self.freq = freq 
        self.val = val 
        self.key = key 

    def insert(self, nex):
        # insert a node to next position  
        nex.pre = self 
        nex.nex = self.nex 
        self.nex.pre = nex 
        self.nex = nex 

def create_linked_list(): 
    head = Node(0,0)
    tail = Node(0,0)
    head.nex = tail 
    tail.pre = head 
    return (head, tail)

class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity 
        self.size = 0 
        self.min_freq = 0
        self.freq_map = defaultdict(create_linked_list)
        self.key_map = {}

    def delete(self, node): 
        if node.pre is not None: 
            # skip the current node 
            node.pre.nex = node.nex 
            node.nex.pre = node.pre 
            
            # check if node is the only element in this freq's linked list 
            # if it is, then self.freq_map[node.freq][0] is head, 
            # self.freq_map[node.freq][-1] is tail  
            if node.pre is self.freq_map[node.freq][0] and node.nex is self.freq_map[node.freq][-1]: 
                self.freq_map.pop(node.freq)
        return node.key

    def increase(self, node): 
        node.freq += 1 
        self.delete(node)
        # insert this node before tail 
        self.freq_map[node.freq][-1].pre.insert(node)
        if node.freq == 1: 
            self.min_freq = 1 
        elif self.min_freq == node.freq - 1: 
            head, tail = self.freq_map[node.freq-1]
            if head.nex is tail:
                # need to update min_freq when min_freq is node.freq - 1 
                # since node's freq is increased by 1  
                self.min_freq = node.freq 

    def get(self, key: int) -> int:
        if key in self.key_map: 
            self.increase(self.key_map[key])
            return self.key_map[key].val 
        return -1 

    def put(self, key: int, value: int) -> None:
        if self.capacity != 0: 
            if key in self.key_map: 
                node = self.key_map[key]
                node.val = value 
            else: 
                node = Node(key, value)
                self.key_map[key] = node 
                self.size += 1 
            
            if self.size > self.capacity: 
                self.size -= 1 
                # delete from head's next, which is the least frequently used node 
                deleted = self.delete(self.freq_map[self.min_freq][0].nex)
                self.key_map.pop(deleted)
                
            self.increase(node)

if __name__ == "__main__": 
    lfu_cache = LFUCache(2)
    result = []

    calls = ["LFUCache", "put", "put", "get", "put", "get", "get", "put", "get", "get", "get"]
    values = [[2], [1, 1], [2, 2], [1], [3, 3], [2], [3], [4, 4], [1], [3], [4]]

    for i in range(len(calls)):
        call = calls[i]
        value = values[i]
        
        if call == "LFUCache":
            lfu_cache = LFUCache(value[0])
            result.append(None)
        elif call == "put":
            lfu_cache.put(value[0], value[1])
            result.append(None)
        elif call == "get":
            result.append(lfu_cache.get(value[0]))

    print(result)