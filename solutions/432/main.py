from typing import * 
from collections import defaultdict 

class Node: 
    def __init__(self, val): 
        self.count = val 
        self.strs = set()
        self.prev = self.next = None 

class AllOne:

    def __init__(self): 
        # map key to count 
        self.key2cnt = defaultdict(int)
        # map count to node 
        self.cnt2node = defaultdict(lambda: None)

        # left = min, right = max 
        self.left = Node(0)
        self.right = Node(0)
        self.left.next = self.right 
        self.right.prev = self.left 

    def add_node(self, key, s, node, after=True):
        self.cnt2node[key] = Node(key)
        self.cnt2node[key].strs.add(s)
        if after:
            next_node = node.next 
        else: 
            next_node = node 
        prev_node = next_node.prev
        prev_node.next = self.cnt2node[key]
        self.cnt2node[key].prev = prev_node
        self.cnt2node[key].next = next_node 
        next_node.prev = self.cnt2node[key]

    def inc(self, key: str) -> None:
        old_count = self.key2cnt[key]
        if old_count != 0: 
            # record previous node, no sorting required
            pre_node = self.cnt2node[old_count]
            pre_node.strs.remove(key)
        else: 
            pre_node = self.left 
        self.key2cnt[key] += 1 
        new_count = self.key2cnt[key]
        if self.cnt2node[new_count] is None: 
            # create new node 
            self.add_node(new_count, key, pre_node)
        else:
            self.cnt2node[new_count].strs.add(key)
        # delete empty node 
        if old_count != 0: 
            if len(pre_node.strs) == 0: 
                # remove empty node 
                pre_node.prev.next = pre_node.next 
                pre_node.next.prev = pre_node.prev
                del self.cnt2node[old_count]

    def dec(self, key: str) -> None:
        old_count = self.key2cnt[key]
        # It is guaranteed that for each call to dec, key is existing in the data structure
        node = self.cnt2node[old_count]
        node.strs.remove(key)
        self.key2cnt[key] -= 1 
        new_count = self.key2cnt[key]
        if new_count == 0: 
            del self.key2cnt[key]
        elif self.cnt2node[new_count] is None: 
            # record next node, no sorting required
            next_node = self.cnt2node[old_count]
            # create new node 
            self.add_node(new_count, key, next_node, after=False)
        else:
            self.cnt2node[new_count].strs.add(key)
        # delete empty node 
        if len(node.strs) == 0: 
            # remove empty node 
            node.prev.next = node.next 
            node.next.prev = node.prev
            del self.cnt2node[old_count]

    def getMaxKey(self) -> str:
        if self.right.prev.prev: 
            return next(iter(self.right.prev.strs))
        else: 
            return ""

    def getMinKey(self) -> str:
        if self.left.next.next: 
            return next(iter(self.left.next.strs))
        else: 
            return ""

if __name__ == "__main__": 
    obj = AllOne()
    obj.inc("hello")
    obj.inc("hello")
    result = obj.getMaxKey()
    assert result == "hello"
    result = obj.getMinKey()
    assert result == "hello"
    obj.inc("leet")
    result = obj.getMaxKey()
    assert result == "hello"
    result = obj.getMinKey()
    assert result == "leet"
    obj.inc("leet")
    obj.inc("leet")
    obj.inc("leet")
    result = obj.getMaxKey()
    assert result == "leet"
    obj.dec("leet")
    obj.dec("leet")
    obj.dec("leet")
    result = obj.getMinKey()
    assert result == "leet"

# ref 

# https://youtu.be/7ABFKPK2hD4