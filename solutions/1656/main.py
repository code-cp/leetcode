from typing import * 

class OrderedStream:

    def __init__(self, n: int):
        self.data = [""] * n 
        self.cur = 0 
        self.len = n 


    def insert(self, idKey: int, value: str) -> List[str]:
        self.data[idKey-1] = value 
        res = []
        for i in range(self.cur, self.len): 
            if len(self.data[i]) != 0:
                res.append(self.data[i])
                self.cur += 1 
            else: 
                break 
        return res 
